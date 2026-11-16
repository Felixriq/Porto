@echo off
echo ========================================================
echo Push Proyek Prediksi Keterlambatan Paket ke GitHub
echo ========================================================
git init
git add streamlit_app.py app.py core.py meta.json model_terlambat.joblib requirements.txt .gitignore README.md
git commit -m "Initial commit: Aplikasi Prediksi Keterlambatan Paket (Streamlit + Flask)"
git branch -M main
git remote remove origin 2>nul
git remote add origin https://github.com/Felixriq/prediksi-keterlambatan-paket.git
git push -u origin main
pause
