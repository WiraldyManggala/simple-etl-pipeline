from utils.extract import mulai_scrape
from utils.transform import transformasi
from utils.load import simpan_ke_csv

URL = 'https://fashion-studio.dicoding.dev/'

if __name__ == "__main__":
    print("Memulai proses ETL...")

    print("1. Ekstraksi data...")
    data_mentah = mulai_scrape(URL)

    print(f"Total data hasil scraping: {len(data_mentah)}")

    print("2. Transformasi data...")
    data_bersih = transformasi(data_mentah)
    print(f"Total data setelah transformasi: {len(data_bersih)}")

    print("3. Load data ke CSV...")
    simpan_ke_csv(data_bersih)

    print("ETL selesai.")
