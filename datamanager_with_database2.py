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

# Fungsi untuk mengubah data ID Operator
def ubah_data_id_operator():
    while True:
        print("Pilih operasi yang ingin Anda lakukan:")
        print("1. Ubah Nama Operator")
        print("2. Ubah NIK Operator")
        print("3. Ubah Sertifikat Kemampuan Proses")
        print("4. Kembali ke Menu Utama")

        pilihan = input("Masukkan nomor operasi yang ingin Anda lakukan (1/2/3/4): ")

        if pilihan == "1":
            ubah_nama_operator()
        elif pilihan == "2":
            ubah_nik_operator()
        elif pilihan == "3":
            ubah_sertifikat_kemampuan()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

def ubah_nama_operator():
    id_data = input("Masukkan ID data ID Operator yang ingin diubah: ")

    cursor.execute("SELECT * FROM id_operator WHERE id=?", (id_data,))
    data = cursor.fetchone()

    if data:
        print(f"Nama Operator saat ini: {data[1]}")
        nama_baru = input("Masukkan Nama Operator yang baru: ")

        cursor.execute("UPDATE id_operator SET nama_operator=? WHERE id=?", (nama_baru, id_data))
        conn.commit()
        print("Nama Operator berhasil diubah.")
    else:
        print(f"ID Operator dengan ID {id_data} tidak ditemukan.")

# Fungsi untuk mengubah NIK Operator
def ubah_nik_operator():
    id_data = input("Masukkan ID data ID Operator yang ingin diubah: ")

    cursor.execute("SELECT * FROM id_operator WHERE id=?", (id_data,))
    data = cursor.fetchone()

    if data:
        print(f"NIK Operator saat ini: {data[2]}")
        nik_baru = input("Masukkan NIK Operator yang baru: ")

        cursor.execute("UPDATE id_operator SET nik_operator=? WHERE id=?", (nik_baru, id_data))
        conn.commit()
        print("NIK Operator berhasil diubah.")
    else:
        print(f"ID Operator dengan ID {id_data} tidak ditemukan.")

# Fungsi untuk mengubah Sertifikat Kemampuan Proses
def ubah_sertifikat_kemampuan():
    id_data = input("Masukkan ID data ID Operator yang ingin diubah: ")

    cursor.execute("SELECT * FROM id_operator WHERE id=?", (id_data,))
    data = cursor.fetchone()

    if data:
        print(f"Sertifikat Kemampuan Proses saat ini: {data[3]}")
        sertifikat_baru = input("Masukkan Sertifikat Kemampuan Proses yang baru: ")

        cursor.execute("UPDATE id_operator SET sertifikat_kemampuan=? WHERE id=?", (sertifikat_baru, id_data))
        conn.commit()
        print("Sertifikat Kemampuan Proses berhasil diubah.")
    else:
        print(f"ID Operator dengan ID {id_data} tidak ditemukan.")

# Fungsi untuk mengubah data ID Station Proses
def ubah_data_id_station_proses():
    while True:
        print("Pilih operasi yang ingin Anda lakukan:")
        print("1. Ubah Nama Proses")
        print("2. Ubah Operator yang Bersertifikat")
        print("3. Kembali ke Menu Utama")

        pilihan = input("Masukkan nomor operasi yang ingin Anda lakukan (1/2/3): ")

        if pilihan == "1":
            ubah_nama_proses()
        elif pilihan == "2":
            ubah_operator_bersertifikat()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

def ubah_nama_proses():
    id_data = input("Masukkan ID data ID Station Proses yang ingin diubah: ")

    cursor.execute("SELECT * FROM id_station_proses WHERE id=?", (id_data,))
    data = cursor.fetchone()

    if data:
        print(f"Nama Proses saat ini: {data[1]}")
        nama_baru = input("Masukkan Nama Proses yang baru: ")

        cursor.execute("UPDATE id_station_proses SET nama_proses=? WHERE id=?", (nama_baru, id_data))
        conn.commit()
        print("Nama Proses berhasil diubah.")
    else:
        print(f"ID Station Proses dengan ID {id_data} tidak ditemukan.")

# Fungsi untuk mengubah Operator yang Bersertifikat
def ubah_operator_bersertifikat():
    id_data = input("Masukkan ID data ID Station Proses yang ingin diubah: ")

    cursor.execute("SELECT * FROM id_station_proses WHERE id=?", (id_data,))
    data = cursor.fetchone()

    if data:
        print(f"Operator yang Bersertifikat saat ini: {data[2]}")
        operator_baru = input("Masukkan Operator yang Bersertifikat yang baru: ")

        cursor.execute("UPDATE id_station_proses SET operator_bersertifikat=? WHERE id=?", (operator_baru, id_data))
        conn.commit()
        print("Operator yang Bersertifikat berhasil diubah.")
    else:
        print(f"ID Station Proses dengan ID {id_data} tidak ditemukan.")

# Fungsi untuk menghapus data ID Operator
def hapus_data_id_operator():
    id_data = input("Masukkan ID data ID Operator yang ingin dihapus: ")

    cursor.execute("SELECT * FROM id_operator WHERE id=?", (id_data,))
    data = cursor.fetchone()

    if data:
        print(f"Data ID Operator yang akan dihapus:")
        print(tabulate([(data[0], data[1], data[2], data[3])], headers=["ID", "Nama Operator", "NIK Operator", "Sertifikat Kemampuan Proses"], tablefmt="grid"))

        konfirmasi = input("Apakah Anda yakin ingin menghapus data ini? (y/n): ")

        if konfirmasi.lower() == "y":
            cursor.execute("DELETE FROM id_operator WHERE id=?", (id_data,))
            conn.commit()
            print("Data ID Operator berhasil dihapus.")
        else:
            print("Data ID Operator tidak dihapus.")
    else:
        print(f"ID Operator dengan ID {id_data} tidak ditemukan.")

# Fungsi untuk menghapus data ID Station Proses
def hapus_data_id_station_proses():
    id_data = input("Masukkan ID data ID Station Proses yang ingin dihapus: ")

    cursor.execute("SELECT * FROM id_station_proses WHERE id=?", (id_data,))
    data = cursor.fetchone()

    if data:
        print(f"Data ID Station Proses yang akan dihapus:")
        print(tabulate([(data[0], data[1], data[2])], headers=["ID", "Nama Proses", "Operator yang Bersertifikat"], tablefmt="grid"))

        konfirmasi = input("Apakah Anda yakin ingin menghapus data ini? (y/n): ")

        if konfirmasi.lower() == "y":
            cursor.execute("DELETE FROM id_station_proses WHERE id=?", (id_data,))
            conn.commit()
            print("Data ID Station Proses berhasil dihapus.")
        else:
            print("Data ID Station Proses tidak dihapus.")
    else:
        print(f"ID Station Proses dengan ID {id_data} tidak ditemukan.")

# Fungsi untuk menampilkan semua data yang tersimpan
def data_yang_tersimpan_id_operator():
    cursor.execute("SELECT * FROM id_operator")
    data = cursor.fetchall()

    if not data:
        print("Tidak ada data ID Operator tersimpan.")
    else:
        print("Data ID Operator yang tersimpan:")
        print(tabulate(data, headers=["ID", "Nama Operator", "NIK Operator", "Sertifikat Kemampuan Proses"], tablefmt="grid"))

# Fungsi untuk menampilkan semua data yang tersimpan
def data_yang_tersimpan_id_station_proses():
    cursor.execute("SELECT * FROM id_station_proses")
    data = cursor.fetchall()

    if not data:
        print("Tidak ada data ID Station Proses tersimpan.")
    else:
        print("Data ID Station Proses yang tersimpan:")
        print(tabulate(data, headers=["ID", "Nama Proses", "Operator yang Bersertifikat"], tablefmt="grid"))

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
    print("1. Masukkan Data ID Operator")
    print("2. Masukkan Data ID Station Proses")
    print("3. Ubah Data ID Operator")
    print("4. Ubah Data ID Station Proses")
    print("5. Hapus Data ID Operator")
    print("6. Hapus Data ID Station Proses")
    print("7. Data yang Tersimpan ID Operator")
    print("8. Data yang Tersimpan ID Station Proses")
    print("9. Generate Barcode ID Operator")
    print("10. Generate Barcode ID Station Proses")
    print("11. Keluar")

if __name__ == "__main__":
    while True:
        tampilkan_menu_utama()
        pilihan_utama = input("Pilih menu utama (1/2/3/4/5/6/7/8/9/10/11): ")

        if pilihan_utama == "1":
            masukkan_id_operator()
        elif pilihan_utama == "2":
            masukkan_id_station_proses()
        elif pilihan_utama == "3":
            ubah_data_id_operator()
        elif pilihan_utama == "4":
            ubah_data_id_station_proses()
        elif pilihan_utama == "5":
            hapus_data_id_operator()
        elif pilihan_utama == "6":
            hapus_data_id_station_proses()
        elif pilihan_utama == "7":
            data_yang_tersimpan_id_operator()
        elif pilihan_utama == "8":
            data_yang_tersimpan_id_station_proses()
        elif pilihan_utama == "9":
            generate_barcode_id_operator()
        elif pilihan_utama == "10":
            generate_barcode_id_station_proses()
        elif pilihan_utama == "11":
            print("Program selesai.")
            conn.close()
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")
