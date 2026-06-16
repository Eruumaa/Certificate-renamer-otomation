# 🎓 Certificate Renamer & PDF Converter

Sebuah *script* otomatisasi berbasis Python untuk mengubah nama (*rename*) file gambar sertifikat secara massal dan mengonversinya langsung menjadi format PDF siap kirim. Sangat cocok digunakan oleh panitia acara, seminar, atau *workshop* untuk menghemat waktu berjam-jam kerja manual! 🚀

## ✨ Fitur Utama
- **Otomatis Rename:** Mengubah nama file berurutan (misal: `1.jpg`, `2.jpg`) menjadi nama peserta secara otomatis berdasarkan urutan di file CSV.
- **Konversi ke PDF:** Mengonversi sertifikat berformat gambar (.jpg) menjadi dokumen (.pdf) dengan kualitas warna RGB yang rapi.
- **Pembersihan Nama Pintar (Sanitizer):** Otomatis mendeteksi dan menghapus karakter ilegal di Windows (seperti `"`, `:`, `?`, `/`) agar terhindar dari *error* saat *rename*.
- **Smart Resume:** Jika proses terhenti di tengah jalan, *script* akan melanjutkan dari file yang belum diproses tanpa harus mengulang dari awal!

## 🛠️ Persyaratan Sistem (*Prerequisites*)
Pastikan komputer kamu sudah terinstal **Python 3**. 
Script ini juga membutuhkan *library* pihak ketiga yaitu `Pillow` untuk memproses gambar.

Buka terminal / Command Prompt dan jalankan perintah berikut untuk menginstal:
```bash
pip install Pillow
📁 Persiapan Folder & Data
Sebelum menjalankan script, pastikan struktur folder kamu terlihat seperti ini:
```
```
📁 Folder-Sertifikat/
 ├── 🐍 main.py             <-- Script utama
 ├── 📊 data_nama.csv       <-- File daftar nama
 ├── 🖼️ 1.jpg               <-- Sertifikat orang ke-1
 ├── 🖼️ 2.jpg               <-- Sertifikat orang ke-2
 ├── 🖼️ 3.jpg               <-- Sertifikat orang ke-3
 └── ... (dan seterusnya)
⚠️ Aturan Penting untuk data_nama.csv:
```

File CSV hanya perlu berisi 1 kolom nama yang memanjang ke bawah. Tidak perlu baris header (seperti "Nama"). Baris pertama akan langsung dianggap sebagai nama untuk 1.jpg. Pastikan urutan nama dari atas ke bawah sudah benar-benar sesuai dengan urutan file 1.jpg, 2.jpg, dan seterusnya.

🚀 Cara Penggunaan
Kumpulkan semua file gambar sertifikat (.jpg), file data_nama.csv, dan main.py ke dalam satu folder yang sama. Buka terminal atau Command Prompt, lalu arahkan ke folder tersebut.

Jalankan script dengan perintah:
```Bash
python main.py
```
Duduk manis dan biarkan script bekerja! Laporan SUCCESS atau ERROR akan muncul di layar terminalmu. Setelah selesai, folder kamu akan otomatis terisi dengan file .jpg dan .pdf yang sudah berganti nama sesuai daftar peserta. 🎉

👨‍💻 Kontributor
Dibuat dengan ❤️ oleh Akil.
Jika ada kendala (seperti salah ketik nama atau salah penomoran), kamu tinggal memperbaiki file yang salah dan jalankan ulang script-nya.
