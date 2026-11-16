"""Aplikasi staf hub: Flask. Jalankan: python app.py -> http://127.0.0.1:5000"""
import os
import sys

# Pastikan modul core.py di folder yang sama selalu terbaca
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, request, jsonify, render_template_string
from core import prediksi  # type: ignore

app = Flask(__name__)

PAGE = """<!doctype html><html lang="id"><meta charset="utf-8"><title>Prediksi Keterlambatan Paket</title>
<style>
body{font-family:system-ui,sans-serif;background:#f4f6f8;margin:0;color:#1d2733}
header{background:#12344d;color:#fff;padding:14px 28px;font-size:18px;font-weight:600}
main{display:flex;gap:24px;padding:24px 28px;max-width:1100px}
.card{background:#fff;border-radius:10px;padding:18px 20px;box-shadow:0 1px 3px #0002}
form{flex:1.2;display:grid;grid-template-columns:1fr 1fr;gap:10px 14px;align-content:start}
label{font-size:12px;color:#51606e;display:block;margin-bottom:2px}
input,select{width:100%;padding:7px;border:1px solid #c5ced6;border-radius:6px;box-sizing:border-box;font-size:14px}
button{grid-column:1/3;padding:10px;background:#1b6ca8;color:#fff;border:0;border-radius:6px;font-size:15px;cursor:pointer}
#out{flex:1;min-height:260px}
.p{font-size:46px;font-weight:700;margin:4px 0}
.badge{display:inline-block;padding:7px 12px;border-radius:6px;color:#fff;font-weight:600}
.AMAN{background:#2e8b57}.KABARI{background:#d98b00}.PRIORITAS{background:#c0392b}
.warn{background:#fff6e0;border-left:4px solid #d98b00;padding:6px 10px;margin:6px 0;font-size:13px}
.err{background:#fdeaea;border-left:4px solid #c0392b;padding:6px 10px;margin:6px 0;font-size:13px}
h3{margin:0 0 8px}
</style>
<header>Prediksi Keterlambatan Paket &middot; Hub Bandung</header>
<main>
<form id="f" class="card">
<div><label>Tanggal pickup</label><input name="tanggal_pickup" type="date" value="2026-07-06" required></div>
<div><label>Jam pickup (7-22)</label><input name="jam_pickup" type="number" min="7" max="22" step="1" value="19" required></div>
<div>
  <label>Kota tujuan</label>
  <input name="kota_tujuan" list="daftar_kota" value="Medan" required>
  <datalist id="daftar_kota">
    <option value="Balikpapan"><option value="Bekasi"><option value="Bogor"><option value="Cirebon">
    <option value="Denpasar"><option value="Jakarta"><option value="Makassar"><option value="Malang">
    <option value="Medan"><option value="Palembang"><option value="Pontianak"><option value="Semarang">
    <option value="Surabaya"><option value="Tasikmalaya"><option value="Yogyakarta">
  </datalist>
</div>
<div><label>Jarak (km) - boleh kosong</label><input name="jarak_km" type="number" step="any" value="1900"></div>
<div><label>Layanan</label><select name="layanan"><option>EXPRESS</option><option>REG</option><option>HEMAT</option></select></div>
<div><label>Janji (hari)</label><input name="janji_hari" type="number" min="1" max="6" step="1" value="3" required></div>
<div><label>Jumlah transit</label><input name="jumlah_transit" type="number" min="1" max="6" step="1" value="4" required></div>
<div><label>Berat (kg)</label><input name="berat_kg" type="number" step="any" value="2.0"></div>
<div><label>Metode bayar</label><select name="metode_bayar"><option>COD</option><option>non_COD</option></select></div>
<div><label>Cuaca saat pickup</label><select name="cuaca_saat_pickup"><option>hujan_lebat</option><option>cerah</option><option>berawan</option><option>hujan</option><option value="">tidak_diketahui</option></select></div>
<div><label>Volume hub hari ini</label><input name="volume_hub_hari" type="number" step="1" value="5400" required></div>
<div><label>Volume kemarin (opsional)</label><input name="vol_kemarin" type="number" step="1" placeholder="Kosong = median"></div>
<button type="submit">Prediksi</button>
</form>
<div id="out" class="card"><h3>Hasil</h3><span style="color:#51606e">Isi data paket lalu tekan Prediksi.</span></div>
</main>
<script>
const f=document.getElementById('f'),o=document.getElementById('out');
f.onsubmit=async e=>{
 e.preventDefault();
 try {
  const resp=await fetch('/api/predict',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(Object.fromEntries(new FormData(f)))});
  const r=await resp.json();
  let h='<h3>Hasil</h3>';
  (r.error||[]).forEach(m=>h+='<div class="err">'+m+'</div>');
  if(r.ok){
   const c=r.rekomendasi.startsWith('AMAN')?'AMAN':r.rekomendasi.startsWith('KABARI')?'KABARI':'PRIORITAS';
   h+='<div style="font-size:13px;color:#51606e">Probabilitas terlambat</div><div class="p">'+(r.probabilitas*100).toFixed(1)+'%</div><span class="badge '+c+'">'+r.rekomendasi+'</span>';
   if(r.lonjakan)h+='<div class="warn">Hari lonjakan volume: risiko keterlambatan tinggi untuk semua paket.</div>';
   if(!r.andal)h+='<div class="warn"><b>Prediksi kurang andal</b> (masukan di luar rentang data latih).</div>';
  } else {
   h+='<div style="margin-top:8px;color:#c0392b"><b>Prediksi tidak dijalankan.</b> Perbaiki masukan.</div>';
  }
  (r.warning||[]).forEach(m=>h+='<div class="warn">'+m+'</div>');
  o.innerHTML=h;
 } catch(err) {
  o.innerHTML='<h3>Hasil</h3><div class="err">Gagal menghubungi server prediksi.</div>';
 }
};
</script></html>"""


@app.get('/')
def index():
    return render_template_string(PAGE)


@app.post('/api/predict')
def api():
    return jsonify(prediksi(request.get_json(force=True, silent=True) or {}))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)