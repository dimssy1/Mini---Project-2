import getpass
from prettytable import PrettyTable

# Data awal
users = {
    'admin': 'adminpass',
    'pembeli': 'pembelipass'
}

# Daftar event contoh
events = [
    {'nama': 'Konser Musik', 'tanggal': '2024-10-30', 'tempat': 'City Centrum'},
    {'nama': 'Pameran Seni', 'tanggal': '2024-11-15', 'tempat': 'Gor Kadrie Oening Serbaguna'},
    {'nama': 'Seminar Peduli Stunting', 'tanggal': '2024-12-05', 'tempat': 'SMA 10 Samarinda'},
]


# Fungsi untuk login
def login():
    print("masukkan 0 pada username dan password untuk keluar dari program")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    if username in users and users[username] == password:
        return username
    elif username == '0':
        SystemExit
    else:
        print("Username atau password salah.")
        return None

# Fungsi untuk admin
def admin_menu():
    while True:
        print("\n=== Menu Admin ===")
        print("1. Tambah Event")
        print("2. Lihat Event")
        print("3. Update Event")
        print("4. Hapus Event")
        print("5. Logout")
        choice = input("Pilih menu: ")

        if choice == '1':
            tambah_event()
            break
        elif choice == '2':
            lihat_event()
        elif choice == '3':
            update_event()
        elif choice == '4':
            hapus_event()
        elif choice == '5':
            break
        else:
            print("Pilihan tidak valid.")

    main()
            

def tambah_event():
    nama = input("Masukkan nama event: ")
    tanggal = input("Masukkan tanggal event: ")
    tempat = input("Masukkan tempat event: ")
    events.append({'nama': nama, 'tanggal': tanggal, 'tempat': tempat})
    print("Event berhasil ditambahkan.")
    admin_menu()

def lihat_event():
    table = PrettyTable()
    table.field_names = ["No", "Nama Event", "Tanggal", "Tempat"]
    for idx, event in enumerate(events):
        table.add_row([idx + 1, event['nama'], event['tanggal'], event['tempat']])
    print(table)


def update_event():
    lihat_event()
    nomor = int(input("Pilih nomor event yang ingin diupdate: ")) - 1
    if 0 <= nomor < len(events):
        events[nomor]['nama'] = input("Masukkan nama event baru: ")
        events[nomor]['tanggal'] = input("Masukkan tanggal event baru: ")
        events[nomor]['tempat'] = input("Masukkan tempat event baru: ")
        print("Event berhasil diupdate.")
    else:
        print("Nomor tidak valid.")
        admin_menu()


def hapus_event():
    lihat_event()
    nomor = int(input("Pilih nomor event yang ingin dihapus: ")) - 1
    if 0 <= nomor < len(events):
        events.pop(nomor)
        print("Event berhasil dihapus.")
    else:
        print("Nomor tidak valid.")
        admin_menu()


# Fungsi untuk pembeli
def pembeli_menu():
    while True:
        print("\n=== Menu Pembeli ===")
        print("1. Lihat Event")
        print("2. Booking Event")
        print("3. Logout")
        choice = input("Pilih menu: ")

        if choice == '1':
            lihat_event()
        elif choice == '2':
            booking_event()
        elif choice == '3':
            break
        else:
            print("Pilihan tidak valid.")

def booking_event():
    lihat_event()
    nomor = int(input("Pilih nomor event yang ingin dibooking: ")) - 1
    if 0 <= nomor < len(events):
        print(f"Anda telah berhasil booking event: {events[nomor]['nama']}")
    else:
        print("Nomor tidak valid.")

# Main program
def main():
    user = login()
    if user:
        if user == 'admin':
            admin_menu()
        elif user == 'pembeli':
            pembeli_menu()

if __name__ == "__main__":
    main()

