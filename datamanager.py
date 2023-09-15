import qrcode
from tabulate import tabulate

# Inisialisasi dictionary untuk menyimpan data
data = {}

# Fungsi untuk memasukkan data ID Operator
def masukkan_id_operator():
    nama_operator = input("Masukkan Nama Operator: ")
    nik_operator = input("Masukkan NIK Operator: ")
    sertifikat_kemampuan = input("Masukkan Sertifikat Kemampuan Proses: ")

    # Menyimpan data ke dalam dictionary
    id_operator = len(data) + 1
    data[id_operator] = {
        'Nama Operator': nama_operator,
        'NIK Operator': nik_operator,
        'Sertifikat Kemampuan Proses': sertifikat_kemampuan
    }
    
    print("Data ID Operator berhasil dimasukkan.")

# Fungsi untuk memasukkan data ID Station Proses
def masukkan_id_station_proses():
    nama_proses = input("Masukkan Nama Proses: ")
    operator_bersertifikat = input("Masukkan Operator yang Bersertifikat: ")

    # Menyimpan data ke dalam dictionary
    id_station_proses = len(data) + 1
    data[id_station_proses] = {
        'Nama Proses': nama_proses,
        'Operator yang Bersertifikat': operator_bersertifikat
    }
    
    print("Data ID Station Proses berhasil dimasukkan.")

# Fungsi untuk mengubah data
def ubah_data():
    id_data = input("Masukkan ID data yang ingin diubah: ")

    if id_data in data:
        print("Data saat ini:")
        print(tabulate(data[id_data].items(), headers=["Nama Kolom", "Nilai"], tablefmt="grid"))

        # Meminta input untuk perubahan
        print("Masukkan perubahan (kosongkan jika tidak ingin mengubah):")
        nama_operator = input(f"Nama Operator ({data[id_data]['Nama Operator']}): ")
        nik_operator = input(f"NIK Operator ({data[id_data]['NIK Operator']}): ")
        sertifikat_kemampuan = input(f"Sertifikat Kemampuan Proses ({data[id_data]['Sertifikat Kemampuan Proses']}): ")

        # Memperbarui data jika input tidak kosong
        if nama_operator:
            data[id_data]['Nama Operator'] = nama_operator
        if nik_operator:
            data[id_data]['NIK Operator'] = nik_operator
        if sertifikat_kemampuan:
            data[id_data]['Sertifikat Kemampuan Proses'] = sertifikat_kemampuan

        print("Data berhasil diubah.")
    else:
        print("ID data tidak ditemukan.")

# Fungsi untuk menghapus data
def hapus_data():
    id_data = input("Masukkan ID data yang ingin dihapus: ")

    if id_data in data:
        del data[id_data]
        print("Data berhasil dihapus.")
    else:
        print("ID data tidak ditemukan.")

# Fungsi untuk menampilkan semua data yang tersimpan
def data_yang_tersimpan():
    if not data:
        print("Tidak ada data tersimpan.")
    else:
        print("Data yang tersimpan:")
        headers = ["Nama Operator", "NIK Operator", "Sertifikat Kemampuan Proses"]
        rows = []

        for id_data, item_data in data.items():
            row = [id_data, item_data["Nama Operator"], item_data["NIK Operator"], item_data["Sertifikat Kemampuan Proses"]]
            rows.append(row)

        print(tabulate(rows, headers=headers, tablefmt="grid"))


# Fungsi untuk generate dan menampilkan barcode ID Operator berdasarkan Nama Operator
def generate_barcode_id_operator():
    nama_operator = input("Masukkan Nama Operator yang tersimpan: ")

    for id_data, values in data.items():
        if 'Nama Operator' in values and values['Nama Operator'] == nama_operator:
            id_operator = id_data
            sertifikat_kemampuan = values['Sertifikat Kemampuan Proses']

            # Gabungkan data ID Operator, Nama Operator, NIK Operator, dan Sertifikat Kemampuan Proses
            data_to_generate = f"ID Operator: {id_operator}\nNama Operator: {nama_operator}\nNIK Operator: {values['NIK Operator']}\nSertifikat Kemampuan Proses: {sertifikat_kemampuan}"

            # Buat objek QRCode dengan data yang akan di-generate
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )

            qr.add_data(data_to_generate)
            qr.make(fit=True)

            # Buat barcode menggunakan pustaka PIL
            img_operator = qr.make_image(fill_color="black", back_color="white")

            # Simpan dan tampilkan barcode
            img_operator.save(f"barcode_IDOperator_{id_operator}.png")
            print(f"Barcode ID Operator berhasil di-generate sebagai 'barcode_IDOperator_{id_operator}.png'.")
            return

    print("Nama Operator tidak ditemukan.")

# Fungsi untuk generate dan menampilkan barcode ID Station Proses berdasarkan Nama Proses
def generate_barcode_id_station_proses():
    nama_proses = input("Masukkan Nama Proses yang tersimpan: ")

    for id_data, values in data.items():
        if 'Nama Proses' in values and values['Nama Proses'] == nama_proses:
            id_station_proses = id_data
            operator_bersertifikat = values['Operator yang Bersertifikat']

            # Gabungkan data ID Station Proses, Nama Proses, dan Operator yang Bersertifikat
            data_to_generate = f"ID Station Proses: {id_station_proses}\nNama Proses: {nama_proses}\nOperator yang Bersertifikat: {operator_bersertifikat}"

            # Buat objek QRCode dengan data yang akan di-generate
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )

            qr.add_data(data_to_generate)
            qr.make(fit=True)

            # Buat barcode menggunakan pustaka PIL
            img_station_proses = qr.make_image(fill_color="black", back_color="white")

            # Simpan dan tampilkan barcode
            img_station_proses.save(f"barcode_IDStationProses_{id_station_proses}.png")
            print(f"Barcode ID Station Proses berhasil di-generate sebagai 'barcode_IDStationProses_{id_station_proses}.png'.")
            return

    print("Nama Proses tidak ditemukan.")

# Fungsi untuk menampilkan menu utama
def tampilkan_menu_utama():
    print("Pilih menu utama:")
    print("1. Masukkan Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Data yang Tersimpan")
    print("5. Generate Barcode ID Operator")
    print("6. Generate Barcode ID Station Proses")
    print("7. Keluar")

if __name__ == "__main__":
    while True:
        tampilkan_menu_utama()
        pilihan_utama = input("Pilih menu utama (1/2/3/4/5/6/7): ")

        if pilihan_utama == "1":
            while True:
                print("Pilih tipe data yang ingin dimasukkan:")
                print("1. ID Operator")
                print("2. ID Station Proses")
                print("3. Kembali ke Menu Utama")

                pilihan_masukkan = input("Pilih jenis data (1/2/3): ")

                if pilihan_masukkan == "1":
                    masukkan_id_operator()
                elif pilihan_masukkan == "2":
                    masukkan_id_station_proses()
                elif pilihan_masukkan == "3":
                    break
                else:
                    print("Pilihan tidak valid. Silakan pilih kembali.")
        elif pilihan_utama == "2":
            ubah_data()
        elif pilihan_utama == "3":
            hapus_data()
        elif pilihan_utama == "4":
            data_yang_tersimpan()
        elif pilihan_utama == "5":
            generate_barcode_id_operator()
        elif pilihan_utama == "6":
            generate_barcode_id_station_proses()
        elif pilihan_utama == "7":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")
