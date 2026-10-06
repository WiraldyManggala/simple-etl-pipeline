# Proyek Membangun ETL Pipeline Sederhana

## Deskripsi
Proyek ini mengimplementasikan pipeline ETL sederhana yang mengambil data produk dari halaman web [Fashion Studio Dicoding](https://fashion-studio.dicoding.dev/), kemudian mentransformasikan data tersebut menjadi format bersih, dan menyimpannya ke dalam file CSV.

## Langkah-langkah ETL

1. **Extract**:
   - Menggunakan library `requests` dan `BeautifulSoup` untuk melakukan web scraping dari halaman produk.
   - Data yang diambil mencakup: nama produk, harga, rating, jumlah warna, ukuran, dan gender.

2. **Transform**:
   - Membersihkan data harga dari simbol (misalnya `Rp`) dan mengubahnya ke format float.
   - Mengubah string rating menjadi float.
   - Menghitung jumlah warna dari daftar warna yang tersedia.
   - Menambahkan timestamp saat data diproses.

3. **Load**:
   - Data yang telah dibersihkan disimpan ke file `products.csv` menggunakan `pandas.DataFrame.to_csv()`.

## Tools & Library yang Digunakan
- Python 3.x
- `requests` untuk mengambil data dari web.
- `beautifulsoup4` untuk parsing HTML.
- `pandas` untuk transformasi dan penyimpanan data.
- `pytest` untuk pengujian unit.

## Cara Menjalankan
1. Instal dependensi yang diperlukan:
   ```bash
   pip install -r requirements.txt
Jalankan program utama ETL:

Bash
python main.py
Testing
Pengujian dilakukan menggunakan pytest.

Output
File hasil akhir adalah products.csv yang berisi data produk dari situs.

Kontributor
Wiraldy Manggala Simanjuntak
