# 🏗️ Computer Vision Datathon – Deteksi Atribut Keselamatan Pekerja

Proyek ini merupakan solusi Computer Vision untuk mendeteksi **atribut keselamatan kerja** pada gambar pekerja di lingkungan **pabrik** dan **konstruksi** menggunakan model **YOLOv8**. Fokus utama adalah mengidentifikasi berbagai **alat pelindung diri (APD)** seperti:

* **Masker**
* **Sarung tangan**
* **Sepatu safety**
* **Kacamata pelindung**
* **Helm keselamatan**
* **Rompi reflektif**

## 📁 Struktur Folder

```
.
├── TRAINING/
│   ├── atribut_pekerjaan_kontruksi/
│   │   └── datathon_helmet_and_jacket.ipynb
│   ├── atribut_pekerjaan_pabrik/
│   │   └── datathon_apd.ipynb
│
├── model/
│   ├── atribut pekerja kontruksi.pt       # Model YOLOv8 hasil training untuk pekerja konstruksi
│   └── atribut pekerja pabrik.pt          # Model YOLOv8 hasil training untuk pekerja pabrik
│
├── main.py                                # Skrip untuk menjalankan inference
├── requirements.txt                       # Daftar dependensi proyek
└── README.md                              # Dokumentasi proyek
```

## 🚀 Teknologi dan Tools

* Python
* [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
* OpenCV
* Pandas
* Matplotlib
* Google Colab / Jupyter Notebook

## 📌 Cara Menjalankan

1. **Clone repositori:**

   ```bash
   git clone https://github.com/Ikram-sabila/Computer-Vision-Datathon.git
   cd Computer-Vision-Datathon
   ```

2. **Install dependensi:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Jalankan Notebook Training (opsional):**

   * `TRAINING/atribut_pekerjaan_kontruksi/datathon_helmet_and_jacket.ipynb`
   * `TRAINING/atribut_pekerjaan_pabrik/datathon_apd.ipynb`

4. **Lakukan Inferensi:**
   Gunakan `main.py` untuk mendeteksi atribut APD pada gambar.

## 📈 Hasil Model

Model YOLOv8 memberikan hasil yang kuat dalam mendeteksi atribut keselamatan:

| Lingkup            | Atribut yang Dideteksi                        | mAP\@0.5 |
| ------------------ | --------------------------------------------- | -------- |
| Pekerja Pabrik     | Masker, Sarung tangan, Sepatu, Kacamata, dll. | \~96%    |
| Pekerja Konstruksi | Helm keselamatan, Rompi reflektif             | \~94%    |

> *Catatan: mAP berdasarkan hasil evaluasi selama pelatihan di dataset masing-masing.*

## 📌 Catatan

* Dataset diunduh otomatis via `gdown` (lihat dalam notebook).
* Model disimpan dalam format `.pt` dan dapat digunakan langsung untuk inferensi.
