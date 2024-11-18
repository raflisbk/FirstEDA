# Panduan Pengaturan Proyek

Ikuti langkah-langkah berikut untuk mengatur dan menjalankan proyek ini.

## Prasyarat
Proyek ini dapat diatur menggunakan berbagai tools Python lainnya. Namun, dalam proyek ini saya menggunakan **Conda** untuk mengelola lingkungan pengembangan.

## Langkah-langkah :

1. **Buka Terminal Perangkat Anda**

2. **Aktifkan Environment Conda Anda**  
   Jika Anda menggunakan Conda, ganti `"your environment"` dengan nama environment Conda Anda, kemudian jalankan perintah berikut:  
   ```bash
   conda activate "your environment"
3. **Install Library yang dibutuhkan**
   Instal semua paket Python yang diperlukan menggunakan file requirement.txt:
   ```bash
   pip install -r requirement.txt
4. **Jalankan Aplikasi Streamlit**
   ```bash
   streamlit run ./dashboard/dashboard.py

   
