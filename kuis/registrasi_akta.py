import json
import os

# =========================================
# SISTEM REGISTRASI AKTA KELAHIRAN
# =========================================

NAMA_FILE = "data_kelahiran.json"


# 1. MEMUAT DATA
def muat_data():
    if os.path.exists(NAMA_FILE):
        try:
            with open(NAMA_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)

                if isinstance(data, list):
                    return data

                print("Format data tidak valid.")
                return []

        except (json.JSONDecodeError, OSError):
            print("File data gagal dibaca.")
            return []

    return []


# 2. MENYIMPAN DATA
def simpan_data(data_kelahiran):
    try:
        with open(NAMA_FILE, "w", encoding="utf-8") as file:
            json.dump(
                data_kelahiran,
                file,
                indent=4,
                ensure_ascii=False
            )
        return True

    except OSError:
        print("Data gagal disimpan.")
        return False


# 3. REGISTRASI DATA KELAHIRAN
def registrasi_akta(data_kelahiran):
    print("\n===== REGISTRASI AKTA KELAHIRAN =====")

    nomor = input("Nomor Registrasi: ").strip()

    if not nomor:
        print("Nomor registrasi wajib diisi!")
        return

    # Memeriksa nomor registrasi ganda
    for data in data_kelahiran:
        if data["Nomor Registrasi"] == nomor:
            print("Nomor registrasi sudah terdaftar!")
            return

    nama_anak = input("Nama Anak: ").strip()
    jenis_kelamin = input(
        "Jenis Kelamin (Laki-laki/Perempuan): "
    ).strip().capitalize()

    tempat_lahir = input("Tempat Lahir: ").strip()
    tanggal_lahir = input("Tanggal Lahir: ").strip()
    nama_ayah = input("Nama Ayah: ").strip()
    nama_ibu = input("Nama Ibu: ").strip()
    alamat = input("Alamat: ").strip()

    if not all([
        nama_anak,
        jenis_kelamin,
        tempat_lahir,
        tanggal_lahir,
        nama_ayah,
        nama_ibu,
        alamat
    ]):
        print("Semua data wajib diisi!")
        return

    if jenis_kelamin not in ["Laki-laki", "Perempuan"]:
        print("Jenis kelamin tidak valid!")
        return

    data_baru = {
        "Nomor Registrasi": nomor,
        "Nama Anak": nama_anak,
        "Jenis Kelamin": jenis_kelamin,
        "Tempat Lahir": tempat_lahir,
        "Tanggal Lahir": tanggal_lahir,
        "Nama Ayah": nama_ayah,
        "Nama Ibu": nama_ibu,
        "Alamat": alamat
    }

    data_kelahiran.append(data_baru)

    if simpan_data(data_kelahiran):
        print("\nData akta kelahiran berhasil disimpan!")
    else:
        data_kelahiran.pop()


# 4. MENAMPILKAN SEMUA DATA
def tampilkan_data(data_kelahiran):
    print("\n===== DAFTAR DATA AKTA KELAHIRAN =====")

    if len(data_kelahiran) == 0:
        print("Belum ada data akta kelahiran.")
        return

    for nomor, data in enumerate(data_kelahiran, start=1):
        print(f"\n========== DATA KE-{nomor} ==========")

        for kolom, isi in data.items():
            print(f"{kolom}: {isi}")

        print("=" * 35)

    print(f"\nJumlah data: {len(data_kelahiran)}")


# 5. MENCARI DATA
def cari_data(data_kelahiran):
    print("\n===== CARI DATA AKTA KELAHIRAN =====")

    nomor = input("Masukkan Nomor Registrasi: ").strip()

    for data in data_kelahiran:
        if data["Nomor Registrasi"] == nomor:
            print("\nDATA DITEMUKAN!")

            for kolom, isi in data.items():
                print(f"{kolom}: {isi}")

            return

    print("Data tidak ditemukan!")


# 6. MENGUBAH DATA
def ubah_data(data_kelahiran):
    print("\n===== UBAH DATA AKTA KELAHIRAN =====")

    nomor = input("Nomor Registrasi: ").strip()

    for data in data_kelahiran:
        if data["Nomor Registrasi"] == nomor:
            print("Kosongkan isian jika tidak ingin mengubahnya.")

            nama = input(
                f"Nama Anak [{data['Nama Anak']}]: "
            ).strip()

            tempat = input(
                f"Tempat Lahir [{data['Tempat Lahir']}]: "
            ).strip()

            tanggal = input(
                f"Tanggal Lahir [{data['Tanggal Lahir']}]: "
            ).strip()

            ayah = input(
                f"Nama Ayah [{data['Nama Ayah']}]: "
            ).strip()

            ibu = input(
                f"Nama Ibu [{data['Nama Ibu']}]: "
            ).strip()

            alamat = input(
                f"Alamat [{data['Alamat']}]: "
            ).strip()

            if nama:
                data["Nama Anak"] = nama

            if tempat:
                data["Tempat Lahir"] = tempat

            if tanggal:
                data["Tanggal Lahir"] = tanggal

            if ayah:
                data["Nama Ayah"] = ayah

            if ibu:
                data["Nama Ibu"] = ibu

            if alamat:
                data["Alamat"] = alamat

            if simpan_data(data_kelahiran):
                print("Data berhasil diubah!")

            return

    print("Data tidak ditemukan!")


# 7. MENGHAPUS DATA
def hapus_data(data_kelahiran):
    print("\n===== HAPUS DATA AKTA KELAHIRAN =====")

    nomor = input("Nomor Registrasi: ").strip()

    for indeks, data in enumerate(data_kelahiran):
        if data["Nomor Registrasi"] == nomor:
            print("Nama Anak:", data["Nama Anak"])

            konfirmasi = input(
                "Yakin menghapus data? (ya/tidak): "
            ).strip().lower()

            if konfirmasi == "ya":
                data_dihapus = data_kelahiran.pop(indeks)

                if simpan_data(data_kelahiran):
                    print("Data berhasil dihapus!")
                else:
                    data_kelahiran.insert(indeks, data_dihapus)

            else:
                print("Penghapusan dibatalkan.")

            return

    print("Data tidak ditemukan!")


# 8. MENU UTAMA
def menu_utama():
    data_kelahiran = muat_data()

    while True:
        print("\n======================================")
        print(" SISTEM REGISTRASI AKTA KELAHIRAN")
        print("======================================")
        print("1. Registrasi Akta Kelahiran")
        print("2. Tampilkan Data Akta Kelahiran")
        print("3. Cari Data Akta Kelahiran")
        print("4. Ubah Data Akta Kelahiran")
        print("5. Hapus Data Akta Kelahiran")
        print("6. Keluar")
        print("======================================")

        pilihan = input("Pilih menu (1-6): ").strip()

        if pilihan == "1":
            registrasi_akta(data_kelahiran)

        elif pilihan == "2":
            tampilkan_data(data_kelahiran)

        elif pilihan == "3":
            cari_data(data_kelahiran)

        elif pilihan == "4":
            ubah_data(data_kelahiran)

        elif pilihan == "5":
            hapus_data(data_kelahiran)

        elif pilihan == "6":
            print("Program selesai. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid! Masukkan angka 1-6.")


# 9. MENJALANKAN PROGRAM
if __name__ == "__main__":
    menu_utama()