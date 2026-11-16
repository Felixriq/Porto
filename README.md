# Prediksi Keterlambatan Paket - Hub Bandung

Aplikasi prediksi probabilitas keterlambatan pengiriman paket dari Hub Bandung berbasis **Scikit-Learn**, tersedia dalam antarmuka **Streamlit** (`streamlit_app.py`) dan **Flask** (`app.py`).

## Struktur File
- `streamlit_app.py` — Antarmuka aplikasi web untuk **Streamlit Community Cloud**.
- `app.py` — Server web lokal berbasis **Flask**.
- `core.py` — Modul validasi input, prapemrosesan fitur, pemuatan model, dan logika ambang keputusan (threshold).
- `meta.json` — Metadata statistik jarak, jumlah transit per kota tujuan, serta batas rentang data latih.
- `model_terlambat.joblib` — Model *machine learning* terlatih untuk estimasi probabilitas keterlambatan.
- `requirements.txt` — Daftar pustaka Python yang dibutuhkan di Streamlit Cloud maupun lokal.
- `.gitignore` — Aturan pengecualian file sementara dan virtual environment Git.
