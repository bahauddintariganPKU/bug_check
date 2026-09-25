# bug_check

# 🌐 Bug Check Provider & Network Diagnostic

Skrip otomatisasi berbasis Python untuk mendeteksi gangguan, menganalisis latensi (*ping spike*), dan melacak rute lompatan jaringan (*traceroute*) pada jaringan data seluler (seperti Tri, Indosat, Telkomsel, XL) maupun koneksi Wi-Fi.

## ✨ Fitur Utama
* **Konektivitas Dasar:** Memeriksa status sambungan ke DNS global (Google & Cloudflare).
* **Deteksi RTO (Request Time Out):** Menemukan titik putus atau hilangnya paket data (*packet loss*) pada infrastruktur operator.
* **Analisis Rute Mendalam:** Melacak jalur lalu lintas data dari perangkat hingga ke server tujuan secara *hop-by-hop*.
* **Multi-Operator:** Kompatibel dengan semua penyedia layanan internet di Indonesia.

## 🚀 Cara Penggunaan

### 1. Prasyarat
Pastikan perangkat Anda sudah terinstal Python versi 3.x. Jika belum, unduh di [python.org](https://python.org).

### 2. Menjalankan Skrip
Buka Terminal atau PowerShell di folder tempat file berada, lalu jalankan perintah berikut:

```bash
python Bug_check_prov.py
```

## 📊 Cara Membaca Hasil Analisis
* **NORMAL (Tersambung):** Jaringan Anda aman dan merespons dengan cepat.
* **BUG/RTO:** Terjadi gangguan atau pemblokiran paket data di titik server tersebut.
* **Lompatan Jalur (*Hop*):** Jika latensi (ms) melonjak tinggi di tengah rute internal operator (misal: `://indosat.com`), berarti server operator di wilayah Anda sedang mengalami kepadatan trafik (*peak hours*).
