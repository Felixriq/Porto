"""Aplikasi Streamlit: Prediksi Keterlambatan Paket - Hub Bandung.
Jalankan lokal: streamlit run streamlit_app.py
"""
import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from core import prediksi  # type: ignore

st.set_page_config(
    page_title="Prediksi Keterlambatan Paket · Hub Bandung",
    page_icon="📦",
    layout="wide",
)

st.markdown(
    """
    <style>
    .badge {
        display: inline-block;
        padding: 8px 14px;
        border-radius: 6px;
        color: #ffffff;
        font-weight: 600;
        font-size: 15px;
        margin-top: 6px;
    }
    .AMAN { background-color: #2e8b57; }
    .KABARI { background-color: #d98b00; }
    .PRIORITAS { background-color: #c0392b; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📦 Prediksi Keterlambatan Paket · Hub Bandung")

DAFTAR_KOTA = [
    "Medan", "Balikpapan", "Bekasi", "Bogor", "Cirebon",
    "Denpasar", "Jakarta", "Makassar", "Malang", "Palembang",
    "Pontianak", "Semarang", "Surabaya", "Tasikmalaya", "Yogyakarta",
]

col_form, col_out = st.columns([1.2, 1], gap="large")

with col_form:
    with st.form("form_prediksi"):
        c1, c2 = st.columns(2)
        with c1:
            tanggal_pickup = st.date_input(
                "Tanggal pickup",
                value=datetime.date(2026, 7, 6),
            )
            kota_pilihan = st.selectbox(
                "Kota tujuan",
                options=DAFTAR_KOTA + ["Lainnya (ketik manual)"],
                index=0,
            )
            if kota_pilihan == "Lainnya (ketik manual)":
                kota_tujuan = st.text_input("Ketik nama kota tujuan", value="")
            else:
                kota_tujuan = kota_pilihan

            layanan = st.selectbox("Layanan", options=["EXPRESS", "REG", "HEMAT"], index=0)
            jumlah_transit = st.number_input("Jumlah transit", min_value=1, max_value=6, value=4, step=1)
            metode_bayar = st.selectbox("Metode bayar", options=["COD", "non_COD"], index=0)
            volume_hub_hari = st.number_input("Volume hub hari ini", min_value=1, value=5400, step=100)

        with c2:
            jam_pickup = st.number_input("Jam pickup (7-22)", min_value=7, max_value=22, value=19, step=1)
            jarak_km = st.text_input("Jarak (km) - boleh kosong", value="1900")
            janji_hari = st.number_input("Janji (hari)", min_value=1, max_value=6, value=3, step=1)
            berat_kg = st.text_input("Berat (kg)", value="2.0")
            cuaca_saat_pickup = st.selectbox(
                "Cuaca saat pickup",
                options=["hujan_lebat", "cerah", "berawan", "hujan", "tidak_diketahui"],
                index=0,
            )
            vol_kemarin = st.text_input("Volume kemarin (opsional, kosong = median)", value="")

        submitted = st.form_submit_button("Prediksi", use_container_width=True, type="primary")

with col_out:
    st.subheader("Hasil")
    if not submitted:
        st.info("Isi data paket di sebelah kiri lalu tekan **Prediksi**.")
    else:
        payload = {
            "tanggal_pickup": tanggal_pickup.strftime("%Y-%m-%d"),
            "jam_pickup": jam_pickup,
            "kota_tujuan": kota_tujuan,
            "jarak_km": jarak_km.strip(),
            "layanan": layanan,
            "janji_hari": janji_hari,
            "jumlah_transit": jumlah_transit,
            "berat_kg": berat_kg.strip(),
            "metode_bayar": metode_bayar,
            "cuaca_saat_pickup": "" if cuaca_saat_pickup == "tidak_diketahui" else cuaca_saat_pickup,
            "volume_hub_hari": volume_hub_hari,
            "vol_kemarin": vol_kemarin.strip(),
        }
        r = prediksi(payload)

        for err_msg in r.get("error", []):
            st.error(err_msg)

        if r.get("ok"):
            prob_pct = r["probabilitas"] * 100
            rek = r["rekomendasi"]
            kelas = (
                "AMAN" if rek.startswith("AMAN")
                else "KABARI" if rek.startswith("KABARI")
                else "PRIORITAS"
            )
            st.metric("Probabilitas Terlambat", f"{prob_pct:.1f}%")
            st.markdown(f'<div class="badge {kelas}">{rek}</div>', unsafe_allow_html=True)

            if r.get("lonjakan"):
                st.warning("Hari lonjakan volume: risiko keterlambatan tinggi untuk semua paket.")
            if not r.get("andal"):
                st.warning("**Prediksi kurang andal** (masukan di luar rentang data latih).")
        else:
            st.error("**Prediksi tidak dijalankan.** Perbaiki masukan.")

        for warn_msg in r.get("warning", []):
            st.warning(warn_msg)
