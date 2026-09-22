**# Hand Landmark Detection ✋

Program deteksi tangan real-time menggunakan **OpenCV** dan **MediaPipe**. Program ini mendeteksi landmark tangan dari webcam, mengenali jari mana saja yang sedang terangkat, lalu menampilkan pesan **"I LOVE YOU SO MUCH"** di layar sesuai kombinasi jari yang diangkat (terinspirasi dari isyarat tangan "I Love You" dalam ASL).

## Fitur

- Deteksi tangan real-time dari webcam menggunakan MediaPipe Hands
- Mendukung deteksi hingga 2 tangan sekaligus
- Menggambar landmark & koneksi tangan pada frame video
- Mendeteksi status terangkat/tidaknya masing-masing jari (jempol, telunjuk, tengah, manis, kelingking)
- Menampilkan teks di layar sesuai jari yang terangkat

## Struktur Proyek

```
handrecognt/
├── handDetection.py   # Modul class HandDetection (wrapper MediaPipe Hands)
├── utama.py           # Program utama: baca webcam, deteksi jari, tampilkan teks
└── README.md
```

## Cara Kerja

- **`handDetection.py`** berisi class `HandDetection` yang membungkus `mediapipe.solutions.hands`. Method `findHandLandMarks()` menerima sebuah frame gambar, memprosesnya, dan mengembalikan frame hasil (dengan gambar landmark jika `draw=True`) beserta list koordinat landmark setiap tangan yang terdeteksi.
- **`utama.py`** membaca frame dari webcam, memanggil `HandDetection` untuk mendapatkan landmark tangan, lalu membandingkan posisi Y ujung jari (*tip*) dengan pangkal jari (*base*) untuk menentukan apakah jari tersebut sedang terangkat.

## Requirements

- Python 3.10
- [OpenCV](https://pypi.org/project/opencv-python/) (`opencv-python`)
- [MediaPipe](https://pypi.org/project/mediapipe/) (`mediapipe`)
- Webcam

## Instalasi

1. Clone repository ini:
   ```bash
   git clone <url-repo-anda>
   cd handrecognt
   ```

2. (Opsional tapi disarankan) buat virtual environment:
   ```bash
   python -m venv env
   # Windows
   env\Scripts\activate
   # macOS/Linux
   source env/bin/activate
   ```

3. Install dependency:
   ```bash
   pip install opencv-python mediapipe
   ```

## Cara Menjalankan

```bash
python utama.py
```

- Jendela webcam akan terbuka dan menampilkan hasil deteksi tangan.
- Angkat jari untuk melihat teks yang sesuai muncul di layar.
- Tekan tombol **`a`** untuk keluar dari program.

## Catatan

- Folder `env/` (virtual environment) dan `__pycache__/` sebaiknya **tidak** ikut di-commit ke GitHub. Tambahkan ke `.gitignore`:
  ```
  env/
  __pycache__/
  *.pyc
  ```

## Lisensi

Bebas digunakan dan dimodifikasi untuk keperluan pembelajaran.**
