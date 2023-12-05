# Automatic-Number-Plate-Recognition

Proyek ini bertujuan untuk melakukan deteksi plat nomor kendaraan pada gambar menggunakan Optical Character Recognition (OCR). Hasil deteksi disimpan dalam database MySQL, dan juga terdapat skrip penampilan untuk menampilkan gambar beserta teks dan ID yang terkait

## Persyaratan

Sebelum menjalankan skrip, pastikan Anda memiliki:

- Python terinstal
- Paket Python yang diperlukan terinstal (`mysql-connector-python`, `matplotlib`, `numpy`, `opencv-python`, `easyocr`, `imutils`, `python-dotenv`)

```bash
pip install mysql-connector-python matplotlib numpy opencv-python easyocr imutils python-dotenv
```

## Penggunaan

1. Clone repositori:

```
git clone https://github.com/roniragilimankhoirul/Automatic-Number-Plate-Recognition.git && cd Automatic-Number-Plate-Recognition
```

2. Buat virtual environment:

```
python -m venv myenv
```

3. Mengaktifkan virtual environments:

```
source myenv/bin/activate
```

4. Instal Dependensi:

```
pip install -r requirements.txt
```

5. Modifikasi file .env:

```
DB_HOST=your_database_host
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=your_database_name
```

6. Jalankan program untuk deteksi plat nomor:

```
python main.py path/to/your/image.jpg
```

7. Jalankan program untuk melihat gambar yang ada di database:

```
python view_image.py [index]
```

- Jika tidak ada indeks yang diberikan, semua gambar akan ditampilkan.
- Jika indeks diberikan, hanya gambar pada indeks tersebut yang akan ditampilkan.

## Versi Bahasa

- [English Version (README.md)](README.md)
- [Indonesian Version (README_ID.md)](README_ID.md)
