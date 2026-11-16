"""Logika inti aplikasi: validasi masukan, pembersihan, prediksi, rekomendasi."""
import json
import os
import numpy as np
import pandas as pd
import joblib

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = joblib.load(os.path.join(HERE, 'model_terlambat.joblib'))
with open(os.path.join(HERE, 'meta.json'), encoding='utf-8') as f:
    META = json.load(f)
ALIAS = {
    'jakarta': 'Jakarta', 'jkt': 'Jakarta', 'dki jakarta': 'Jakarta',
    'kota bekasi': 'Bekasi', 'di yogyakarta': 'Yogyakarta',
    'jogja': 'Yogyakarta', 'yogya': 'Yogyakarta',
    'sby': 'Surabaya', 'bali': 'Denpasar'
}
KOTA = set(META['jarak'])
T_KABARI = 5000 / (5000 + 50000)   # 0,0909 dari biaya FP=Rp5.000, FN=Rp50.000
T_PRIORITAS = 0.50
TIPE_SLA = {'EXPRESS': (1, 3), 'REG': (2, 4), 'HEMAT': (4, 6)}
CUACA = {'cerah', 'berawan', 'hujan', 'hujan_lebat'}


def _num(v):
    try:
        if v is None or str(v).strip() == '':
            return None
        val = float(v)
        if np.isnan(val) or np.isinf(val):
            return 'bad'
        return val
    except Exception:
        return 'bad'


def prediksi(p: dict):
    """Return dict: ok, error(list), warning(list), probabilitas, rekomendasi, andal(bool), lonjakan(bool)."""
    err, warn = [], []

    # 1. Tanggal
    tgl_raw = p.get('tanggal_pickup')
    tgl = pd.to_datetime(tgl_raw, format='%Y-%m-%d', errors='coerce')
    if pd.isna(tgl):
        tgl = pd.to_datetime(tgl_raw, errors='coerce')
    if pd.isna(tgl):
        err.append('Tanggal pickup tidak valid (format YYYY-MM-DD).')

    # 2. Jam pickup
    jam = _num(p.get('jam_pickup'))
    if jam in (None, 'bad') or jam != int(jam):
        err.append('Jam pickup harus bilangan bulat.')
    elif not 7 <= jam <= 22:
        err.append('Jam pickup di luar jam operasional (7-22).')

    # 3. Kota tujuan
    k = str(p.get('kota_tujuan', '') or '').strip().lower()
    kota = ALIAS.get(k, k.title())
    kota_dikenal = kota in KOTA
    if not k:
        err.append('Kota tujuan wajib diisi.')
    elif not kota_dikenal:
        warn.append(f'Kota "{p.get("kota_tujuan")}" tidak ada di data latih; model tidak punya pola khusus kota ini.')

    # 4. Layanan & metode bayar
    lay = str(p.get('layanan', '') or '').strip().upper()
    if lay == 'EXP':
        lay = 'EXPRESS'
    if lay not in TIPE_SLA:
        err.append('Layanan harus EXPRESS, REG, atau HEMAT.')

    mb = str(p.get('metode_bayar', '') or '').strip()
    if mb.upper() == 'COD':
        mb = 'COD'
    elif mb.lower() in ('non_cod', 'non-cod', 'non cod'):
        mb = 'non_COD'
    else:
        err.append('Metode bayar harus COD atau non_COD.')

    # 5. Janji hari & jumlah transit
    jj = _num(p.get('janji_hari'))
    jt = _num(p.get('jumlah_transit'))
    if jj in (None, 'bad') or jj != int(jj) or not 1 <= jj <= 6:
        err.append('Janji hari harus bilangan bulat 1-6.')
    elif lay in TIPE_SLA and not TIPE_SLA[lay][0] <= jj <= TIPE_SLA[lay][1]:
        warn.append(f'Janji {int(jj)} hari tidak lazim untuk layanan {lay}; periksa kembali.')

    if jt in (None, 'bad') or jt != int(jt) or not 1 <= jt <= 6:
        err.append('Jumlah transit harus bilangan bulat 1-6.')
    elif kota_dikenal and not META['transit'][kota]['min'] <= jt <= META['transit'][kota]['max']:
        warn.append(f'Jumlah transit {int(jt)} tidak lazim untuk tujuan {kota}.')

    # 6. Jarak (km)
    jr_input = _num(p.get('jarak_km'))
    jr = jr_input
    if jr == 'bad' or (jr is not None and not 0 < jr <= 2500):
        err.append('Jarak (km) harus angka antara 0 dan 2.500.')
        jr = None
    elif jr is None:
        if kota_dikenal:
            jr = META['jarak'][kota]['median']
            warn.append(f'Jarak kosong; diisi median tujuan {kota} ({int(jr)} km).')
        else:
            err.append('Jarak wajib diisi untuk kota yang tidak dikenal.')
    elif kota_dikenal:
        a = META['jarak'][kota]
        if not a['min'] * 0.8 <= jr <= a['max'] * 1.2:
            warn.append(f'Jarak {int(jr)} km tidak sesuai kisaran {kota} ({int(a["min"])}-{int(a["max"])} km).')

    # 7. Berat (kg)
    b_input = _num(p.get('berat_kg'))
    b = b_input
    berat_gram_salah = 0
    if b == 'bad':
        err.append('Berat harus angka.')
        b = None
    elif b is None or b <= 0:
        warn.append(f'Berat kosong/tidak valid; diisi median ({META["berat_median"]} kg).')
        b = META['berat_median']
    else:
        if b >= 100:
            warn.append(f'Berat {b:g} dianggap gram (bukan kg) dan dikonversi menjadi {b/1000:g} kg.')
            b = b / 1000.0
            berat_gram_salah = 1
        if b > META['berat_max']:
            warn.append(f'Berat {b:g} kg melebihi rentang data latih (maks {META["berat_max"]:.0f} kg).')

    # 8. Volume hub hari ini & kemarin
    vol = _num(p.get('volume_hub_hari'))
    if vol in (None, 'bad') or vol <= 0:
        err.append('Volume hub hari ini wajib berupa angka positif.')
    elif not META['vol_min'] <= vol <= META['vol_max']:
        warn.append(
            f'Volume {int(vol)} di luar rentang data latih ({META["vol_min"]}-{META["vol_max"]}); '
            f'prediksi kurang andal (nilai dipotong ke batas data latih).'
        )

    vk = _num(p.get('vol_kemarin'))
    if vk == 'bad' or (vk is not None and vk <= 0):
        warn.append('Volume kemarin tidak valid; diisi median.')
        vk = META['vol_median']
    elif vk is None:
        vk = META['vol_median']
    else:
        vk = float(np.clip(vk, META['vol_min'], META['vol_max']))

    # 9. Cuaca
    cu_raw = str(p.get('cuaca_saat_pickup', '') or '').strip().lower()
    cu = cu_raw
    if cu not in CUACA:
        if cu and cu != 'tidak_diketahui':
            warn.append(f'Cuaca "{cu}" tidak dikenali; diperlakukan sebagai tidak diketahui.')
        cu = 'tidak_diketahui'

    if err:
        return {'ok': False, 'error': err, 'warning': warn}

    vol_asli = vol
    vol = float(np.clip(vol, META['vol_min'], META['vol_max']))

    # Susun 30 kolom sesuai urutan asli saat model_terlambat.joblib dilatih
    d = pd.DataFrame([dict(
        id_resi='DUMMY',
        tanggal_pickup=str(tgl_raw),
        jam_pickup=int(jam),
        kota_tujuan=str(p.get('kota_tujuan', '')),
        jarak_km=float(jr),
        jumlah_transit=int(jt),
        layanan=lay,
        janji_hari=int(jj),
        berat_kg=float(b),
        metode_bayar=mb,
        cuaca_saat_pickup=cu_raw,
        volume_hub_hari=vol,
        terlambat=0,
        tanggal=tgl,
        kota=kota,
        berat_gram_salah=berat_gram_salah,
        berat_kg_clean=float(b),
        jarak_missing=int(jr_input is None),
        jarak=float(jr),
        cuaca=cu,
        dow=int(tgl.dayofweek),
        senin=int(tgl.dayofweek == 0),
        after_cutoff=int(jam >= 17),
        slack=int(jj - jt),
        hari_per_1000km=float(jj / (jr / 1000.0)),
        surge=int(vol_asli > 9000),
        hujan_lebat=int(cu == 'hujan_lebat'),
        log_vol=float(np.log(vol)),
        berat=float(b),
        vol_kemarin=float(vk)
    )])

    pr = float(MODEL.predict_proba(d)[:, 1][0])
    if pr >= T_PRIORITAS:
        rek = 'PRIORITASKAN + KABARI PELANGGAN'
    elif pr >= T_KABARI:
        rek = 'KABARI PELANGGAN (kemungkinan terlambat)'
    else:
        rek = 'AMAN'

    andal = not any(
        'di luar rentang' in w or 'tidak ada di data latih' in w or 'melebihi' in w
        for w in warn
    )
    return {
        'ok': True,
        'probabilitas': round(pr, 4),
        'rekomendasi': rek,
        'warning': warn,
        'andal': andal,
        'lonjakan': bool(vol_asli > 9000)
    }