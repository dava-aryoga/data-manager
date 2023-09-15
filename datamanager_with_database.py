import sqlite3
import qrcode
from tabulate import tabulate

# Inisialisasi koneksi ke database SQLite
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Buat tabel ID Operator jika belum ada
cursor.execute('''
    CREATE TABLE IF NOT EXISTS id_operator (
        id INTEGER PRIMARY KEY,
        nama_operator TEXT,
        nik_operator TEXT,
        sertifikat_kemampuan TEXT
    )
''')

# Buat tabel ID Station Proses jika belum ada
cursor.execute('''
    CREATE TABLE IF NOT EXISTS id_station_proses (
        id INTEGER PRIMARY KEY,
        nama_proses TEXT,
        operator_bersertifikat TEXT
    )
''')

# Fungsi untuk memasukkan data ID Operator ke database
def masukkan_id_operator():
    nama_operator = input("Masukkan Nama Operator: ")
    nik_operator = input("Masukkan NIK Operator: ")
    sertifikat_kemampuan = input("Masukkan Sertifikat Kemampuan Proses: ")

    cursor.execute("INSERT INTO id_operator (nama_operator, nik_operator, sertifikat_kemampuan) VALUES (?, ?, ?)",
                   (nama_operator, nik_operator, sertifikat_kemampuan))
    conn.commit()
    print("Data ID Operator berhasil dimasukkan.")

# Fungsi untuk memasukkan data ID Station Proses ke database
def masukkan_id_station_proses():
    nama_proses = input("Masukkan Nama Proses: ")
    operator_bersertifikat = input("Masukkan Operator yang Bersertifikat: ")

    cursor.execute("INSERT INTO id_station_proses (nama_proses, operator_bersertifikat) VALUES (?, ?)",
                   (nama_proses, operator_bersertifikat))
    conn.commit()
    print("Data ID Station Proses berhasil dimasukkan.")

# Fungsi untuk mengubah data
def ubah_data():
    jenis_data = input("Masukkan jenis data yang ingin diubah (ID Operator/ID Station Proses): ").lower()
    id_data = input(f"Masukkan ID data {jenis_data} yang ingin diubah: ")

    if jenis_data == "id operator":
        tabel = "id_operator"
    elif jenis_data == "id station proses":
        tabel = "id_station_proses"
    else:
        print("Jenis data tidak valid.")
        return

    cursor.execute(f"SELECT * FROM {tabel} WHERE id=?", (id_data,))
    data = cursor.fetchone()

    if data:
        print("Data saat ini:")
        headers = [desc[0] for desc in cursor.description]
        print(tabulate([data], headers=headers, tablefmt="grid"))

        # Meminta input untuk perubahan
        print("Masukkan perubahan (kosongkan jika tidak ingin mengubah):")
        if jenis_data == "id operator":
            nama_operator = input(f"Nama Operator ({data[1]}): ")
            nik_operator = input(f"NIK Operator ({data[2]}): ")
            sertifikat_kemampuan = input(f"Sertifikat Kemampuan Proses ({data[3]}): ")

            # Memperbarui data jika input tidak kosong
            if nama_operator:
                cursor.execute("UPDATE id_operator SET nama_operator=? WHERE id=?", (nama_operator, id_data))
            if nik_operator:
                cursor.execute("UPDATE id_operator SET nik_operator=? WHERE id=?", (nik_operator, id_data))
            if sertifikat_kemampuan:
                cursor.execute("UPDATE id_operator SET sertifikat_kemampuan=? WHERE id=?", (sertifikat_kemampuan, id_data))
        elif jenis_data == "id station proses":
            nama_proses = input(f"Nama Proses ({data[1]}): ")
            operator_bersertifikat = input(f"Operator yang Bersertifikat ({data[2]}): ")

            # Memperbarui data jika input tidak kosong
            if nama_proses:
                cursor.execute("UPDATE id_station_proses SET nama_proses=? WHERE id=?", (nama_proses, id_data))
            if operator_bersertifikat:
                cursor.execute("UPDATE id_station_proses SET operator_bersertifikat=? WHERE id=?", (operator_bersertifikat, id_data))

        conn.commit()
        print("Data berhasil diubah.")
    else:
        print(f"{jenis_data} dengan ID {id_data} tidak ditemukan.")

# Fungsi untuk menghapus data
def hapus_data():
    jenis_data = input("Masukkan jenis data yang ingin dihapus (ID Operator/ID Station Proses): ").lower()
    id_data = input(f"Masukkan ID data {jenis_data} yang ingin dihapus: ")

    if jenis_data == "id operator":
        tabel = "id_operator"
    elif jenis_data == "id station proses":
        tabel = "id_station_proses"
    else:
        print("Jenis data tidak valid.")
        return

    cursor.execute(f"SELECT * FROM {tabel} WHERE id=?", (id_data,))
    data = cursor.fetchone()

    if data:
        cursor.execute(f"DELETE FROM {tabel} WHERE id=?", (id_data,))
        conn.commit()
        print(f"{jenis_data} dengan ID {id_data} berhasil dihapus.")
    else:
        print(f"{jenis_data} dengan ID {id_data} tidak ditemukan.")

# Fungsi untuk menampilkan semua data yang tersimpan
def data_yang_tersimpan():
    jenis_data = input("Tampilkan data ID Operator atau ID Station Proses (ID Operator/ID Station Proses): ").lower()

    if jenis_data == "id operator":
        tabel = "id_operator"
        headers = ["No", "Nama Operator", "NIK Operator", "Sertifikat Kemampuan Proses"]
    elif jenis_data == "id station proses":
        tabel = "id_station_proses"
        headers = ["No", "Nama Proses", "Operator yang Bersertifikat"]
    else:
        print("Jenis data tidak valid.")
        return

    cursor.execute(f"SELECT * FROM {tabel}")
    data = cursor.fetchall()

    if not data:
        print(f"Tidak ada data {jenis_data} tersimpan.")
    else:
        print(f"Data {jenis_data} yang tersimpan:")
        rows = []

        for row in data:
            rows.append(row)

        print(tabulate(rows, headers=headers, tablefmt="grid"))

# Fungsi untuk generate dan menampilkan barcode ID Operator berdasarkan Nama Operator
def generate_barcode_id_operator():
    nama_operator = input("Masukkan Nama Operator yang tersimpan: ")

    cursor.execute("SELECT * FROM id_operator WHERE nama_operator=?", (nama_operator,))
    data = cursor.fetchone()

    if data:
        id_operator = data[0]
        sertifikat_kemampuan = data[3]

        # Gabungkan data ID Operator, Nama Operator, NIK Operator, dan Sertifikat Kemampuan Proses
        data_to_generate = f"ID Operator: {id_operator}\nNama Operator: {nama_operator}\nNIK Operator: {data[2]}\nSertifikat Kemampuan Proses: {sertifikat_kemampuan}"

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
    else:
        print("Nama Operator tidak ditemukan.")

# Fungsi untuk generate dan menampilkan barcode ID Station Proses berdasarkan Nama Proses
def generate_barcode_id_station_proses():
    nama_proses = input("Masukkan Nama Proses yang tersimpan: ")

    cursor.execute("SELECT * FROM id_station_proses WHERE nama_proses=?", (nama_proses,))
    data = cursor.fetchone()

    if data:
        id_station_proses = data[0]
        operator_bersertifikat = data[2]

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
    else:
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

# Tutup koneksi ke database saat program selesai
conn.close()
