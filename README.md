# SimpliciText

**SimpliciText** adalah aplikasi web berbasis Flask yang dirancang untuk menyederhanakan teks panjang menjadi ringkasan yang mudah dipahami. Dengan menggunakan teknologi pemrosesan bahasa alami (NLP), SimpliciText membantu Anda menangkap inti dari sebuah teks hanya dalam beberapa detik. untuk saat ini aplikasi ini hanya dapat support pada teks dengan bahasa inggris

---

## 🎯 **Fitur Utama**

- **Ringkasan Otomatis:** Buat ringkasan singkat dari teks panjang secara instan.
- **Antarmuka Sederhana:** Desain UI yang intuitif dan mudah digunakan.
- **Dukungan Multi-Bahasa:** Mendukung teks dalam berbagai bahasa.
- **Akses Cepat:** Tidak perlu mendaftar, cukup unggah teks dan dapatkan hasilnya.

---

## 🛠️ **Teknologi yang Digunakan**

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Pemrosesan Bahasa Alami (NLP):** NLTK, SpaCy, atau Hugging Face Transformers

---

## 📦 **Instalasi Lokal**

Ikuti langkah-langkah berikut untuk menjalankan SimpliciText di lingkungan lokal Anda:

### 1. Clone Repository
```bash
git clone https://github.com/Sramadhan7221/kelompok3-SimpliciText.git
cd kelompok3-SimpliciText
```

### 2. Buat Virtual Environment
```bash
python -m venv venv
source venv/bin/activate    # Untuk Linux/Mac
venv\Scripts\activate      # Untuk Windows
```

### 3. Install Dependensi
```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi
```bash
flask run
```
Aplikasi akan tersedia di [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## 🚀 **Cara Penggunaan**

1. Masukkan teks panjang Anda di kolom input.
2. Klik tombol **"Ringkas"**.
3. Lihat ringkasan singkat dari teks Anda.
4. Link video tutorial : https://drive.google.com/file/d/1t2TSGKK_Pw-US0xnbfMazwpbJ1FpUwbB/view?usp=sharing

---

## 📂 **Struktur Proyek**

```
SimpliciText/
├── app.py               # File utama Flask
├── templates/           # File HTML untuk frontend
│   ├── base.html        # Template utama
│   ├── index.html       # Halaman utama
├── static/              # File statis (CSS, JS, gambar)
├── models/              # Logika pemrosesan teks
├── requirements.txt     # Daftar dependensi Python
├── README.md            # Dokumentasi proyek
```

---

## 🧩 **Kontribusi**

Kami sangat menyambut kontribusi dari komunitas! Jika Anda ingin membantu meningkatkan SimpliciText:

1. Fork repository ini.
2. Buat branch baru:
   ```bash
   git checkout -b fitur-baru
   ```
3. Lakukan perubahan dan commit:
   ```bash
   git commit -m "Menambahkan fitur baru"
   ```
4. Push branch Anda:
   ```bash
   git push origin fitur-baru
   ```
5. Ajukan pull request.

---

## ⚖️ **Lisensi**

SimpliciText dilisensikan di bawah [MIT License](LICENSE). Anda bebas menggunakan, memodifikasi, dan mendistribusikan proyek ini dengan menyertakan atribusi.

---

Terima kasih telah menggunakan **SimpliciText**! 😊
