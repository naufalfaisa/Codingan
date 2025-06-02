import os

FILE_NAME = "database_todolist.txt"

# Clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Load data dari database
def load_todo():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        data = []
        for line in file:
            parts = line.strip().split('|')
            if len(parts) == 4:
                tugas, penting, deadline, status = parts
                data.append({
                    'tugas': tugas,
                    'urgen': penting,
                    'deadline': deadline,
                    'status': status
                })
        return data

# Simpan data ke database
def save_todo(todo_list):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for item in todo_list:
            file.write(f"{item['tugas']}|{item['urgen']}|{item['deadline']}|{item['status']}\n")

# Tampilkan To-Do List
def tampilkan_todo(todo_list):
    while True:
        clear_screen()
        print("<< To-Do List >>")

        # Urutkan todo_list: Urgent di atas
        sorted_list = sorted(todo_list, key=lambda x: x['urgen'] != "Urgent")

        if not sorted_list:
            print("\n> Tugas Kosong")
        else:
            print("\nTugas:")
            for i, item in enumerate(sorted_list, start=1):
                print(f"[{i}] {item['tugas']} | {item['urgen']} | {item['deadline']} | {item['status']}")

        input("\nENTER untuk keluar")
        return

# Tambah Tugas
def tambah_tugas(todo_list):
    while True:
        clear_screen()
        print("<< Tambah Tugas >>")
        tugas = input("\n> Masukkan tugas baru: ").strip()
        urgen = input("> Apakah tugas ini urgen? (Y/N): ").strip().capitalize()
        deadline = input("> Masukkan tenggat waktu (Tgl-Bln-Thn): ").strip().capitalize()

        if urgen == "Y":
            urgen_label = "Urgent"
        elif urgen == "N":
            urgen_label = "Not urgent"
        else:
            urgen_label = urgen  # fallback jika input tidak sesuai

        if tugas and urgen and deadline:
            todo_list.append({
                'tugas': tugas,
                'urgen': urgen_label,
                'deadline': deadline,
                'status': "Belum selesai"
            })
            save_todo(todo_list)
            while True:
                clear_screen()
                print("<< Tambah Tugas >>")
                print("\n> Tugas berhasil ditambahkan :)")
                print("\nMenu:")
                print("[1] kembali")
                print("[2] Keluar")
                pilihan = input("\nPilih: ")
                if pilihan == "1":
                    break
                elif pilihan == "2":
                    return
                else:
                    continue
        else:
            while True:
                clear_screen()
                print("<< Tambah Tugas >>")
                print("\n> Input salah!")
                print("\nMenu:")
                print("[1] Ulangi")
                print("[2] Keluar")
                pilihan = input("\nPilih: ")
                if pilihan == "1":
                    break
                elif pilihan == "2":
                    return
                else:
                    continue

# Hapus Tugas
def hapus_tugas(todo_list):
    while True:
        clear_screen()
        print("<< Hapus Tugas >>")
        if not todo_list:
            print("\n> Tugas kosong")
            input("\nENTER untuk keluar")
            return
        else:
            print("\nTo-Do List:")
            for i, item in enumerate(todo_list, start=1):
                print(f"[{i}] {item['tugas']} | {item['urgen']} | {item['deadline']} | {item['status']}")
        try:
            nomor = int(input("\nMasukkan nomor tugas yang ingin dihapus: "))
            if 1 <= nomor <= len(todo_list):
                tugas = todo_list.pop(nomor - 1)
                save_todo(todo_list)
                while True:
                    clear_screen()
                    print("<< Hapus Tugas >>")
                    print(f"\n> Tugas '{tugas['tugas']}' berhasil dihapus.")
                    print("\nMenu:")
                    print("[1] Kembali")
                    print("[2] Keluar")
                    pilihan = input("\nPilih: ")
                    if pilihan == "1":
                        break
                    elif pilihan == "2":
                        return
                    else:
                        continue
            else:
                raise ValueError
        except ValueError:
            while True:
                clear_screen()
                print("<< Hapus Tugas >>")
                print("\n> Nomor tugas tidak valid!")
                print("\nMenu:")
                print("[1] Kembali")
                print("[2] Keluar")
                pilihan = input("\nPilih: ")
                if pilihan == "1":
                    break
                elif pilihan == "2":
                    return
                else:
                    continue

# Tandai tugas selesai
def tandai_selesai(todo_list):
    while True:
        clear_screen()
        print("<< Tandai Tugas Selesai >>")
        if not todo_list:
            print("\n> Tugas kosong")
            input("\nENTER untuk keluar")
            return
        else:
            print("\nTugas:")
            for i, item in enumerate(todo_list, start=1):
                print(f"[{i}] {item['tugas']} | {item['urgen']} | {item['deadline']} | {item['status']}")
        try:
            nomor = int(input("\nMasukkan nomor tugas yang ingin ditandai selesai: "))
            if 1 <= nomor <= len(todo_list):
                todo_list[nomor - 1]['status'] = "Selesai"
                save_todo(todo_list)
                while True:
                    clear_screen()
                    print("<< Tandai Tugas Selesai >>")
                    print(f"\n> Tugas '{todo_list[nomor - 1]['tugas']}' ditandai sebagai selesai.")
                    print("\nMenu:")
                    print("[1] Kembali")
                    print("[2] Keluar")
                    pilihan = input("\nPilih: ")
                    if pilihan == "1":
                        break
                    elif pilihan == "2":
                        return
                    else:
                        continue
            else:
                raise ValueError
        except ValueError:
            while True:
                clear_screen()
                print("<< Tandai Tugas Selesai >>")
                print("\n> Masukkan nomor yang valid!")
                print("\nMenu:")
                print("[1] Kembali")
                print("[2] Keluar")
                pilihan = input("\nPilih: ")
                if pilihan == "1":
                    break
                elif pilihan == "2":
                    return
                else:
                    continue

# Menu utama
def menu():
    todo_list = load_todo()
    while True:
        clear_screen()
        print("<< Selamat Datang di To-Do List >>")
        print("\nSilakan pilih menu:")
        print("[1] Tampilkan To-Do List")
        print("[2] Tambah Tugas")
        print("[3] Hapus Tugas")
        print("[4] Tandai Tugas Selesai")
        print("[5] Tutup")

        pilihan = input("\nPilih: ")

        if pilihan == "1":
            tampilkan_todo(todo_list)
        elif pilihan == "2":
            tambah_tugas(todo_list)
        elif pilihan == "3":
            hapus_tugas(todo_list)
        elif pilihan == "4":
            tandai_selesai(todo_list)
        elif pilihan == "5":
            clear_screen()
            print("<< Terima kasih telah menggunakan To-Do List :) >>")
            break
        else:
            print("\n> Pilihan tidak valid!, pilih yang benar! >:(")
            input("\nENTER untuk ulangi")

# Jalankan program
menu()