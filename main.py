import os
import re
try:
    from PIL import Image
except ImportError:
    print("[ERROR] Modul Pillow belum terinstall!")
    print("Buka terminal dan ketik: pip install Pillow")
    exit()

def bersihkan_nama_file(nama):
    # Menghapus karakter yang dilarang Windows
    return re.sub(r'[<>:"/\\|?*]', '', nama)

def proses_gambar_ke_pdf():
    folder_path = '.' 
    data_file = 'data_nama.csv'

    if not os.path.exists(data_file):
        print(f"[ERROR] File {data_file} tidak ditemukan!")
        return

    with open(data_file, mode='r', encoding='utf-8-sig') as file:
        daftar_nama = [line.strip() for line in file.readlines() if line.strip()]

    print(f"[*] Memproses {len(daftar_nama)} data untuk dikonversi ke PDF...\n")

    for index, nama_baru in enumerate(daftar_nama, start=1):
        nama_baru_bersih = bersihkan_nama_file(nama_baru)
        
        # Mendefinisikan kemungkinan nama file
        nama_angka = f"{index}.jpg"
        nama_rename = f"{nama_baru_bersih}.jpg"
        nama_pdf = f"{nama_baru_bersih}.pdf"
        
        path_angka = os.path.join(folder_path, nama_angka)
        path_rename = os.path.join(folder_path, nama_rename)
        path_pdf = os.path.join(folder_path, nama_pdf)
        
        # Tentukan file mana yang akan diproses (memprioritaskan yang sudah di-rename)
        file_sumber = None
        if os.path.exists(path_rename):
            file_sumber = path_rename
        elif os.path.exists(path_angka):
            file_sumber = path_angka
            
        if file_sumber:
            try:
                # 1. Buka file gambar
                gambar = Image.open(file_sumber)
                
                # 2. Konversi format warna ke RGB (wajib untuk PDF)
                gambar_rgb = gambar.convert("RGB")
                
                # 3. Simpan sebagai file PDF
                gambar_rgb.save(path_pdf)
                print(f"[SUCCESS] PDF Dibuat: {nama_pdf}")
                
                # Menutup akses gambar agar file aslinya bisa di-rename jika diperlukan
                gambar.close() 
                
                # Jika file masih pakai angka (contoh 55.jpg), sekalian di-rename ke nama orang
                if file_sumber == path_angka:
                    os.rename(path_angka, path_rename)
                    
            except Exception as e:
                print(f"[ERROR] Gagal memproses {nama_baru_bersih}: {e}")
        else:
            print(f"[WARNING] File foto untuk '{nama_baru_bersih}' tidak ditemukan!")

    print("\n[*] Semua proses selesai!")

if __name__ == '__main__':
    proses_gambar_ke_pdf()