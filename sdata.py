import os

def menu():
    print("\n======================")
    print(" SMART FILE BOT 📁")
    print("======================")
    print("1. Lihat file")
    print("2. Buat folder")
    print("3. Hapus file")
    print("4. Cek lokasi sekarang")
    print("0. Keluar")
    print("======================")

while True:
    menu()
    pilih = input("Pilih: ")

    # 📁 lihat file
    if pilih == "1":
        os.system("ls")

    # 📂 buat folder
    elif pilih == "2":
        nama = input("Nama folder: ")
        os.system(f"mkdir {nama}")
        print("✔ Folder dibuat")

    # ❌ hapus file
    elif pilih == "3":
        nama = input("Nama file: ")
        os.system(f"rm -i {nama}")

    # 📍 lokasi
    elif pilih == "4":
        os.system("pwd")

    # 🚪 keluar
    elif pilih == "0":
        print("Keluar...")
        break

    else:
        print("Pilihan tidak valid")
