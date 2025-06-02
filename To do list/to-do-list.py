import os

# File database
FILE_NAME = "database_todolist.txt"

# Simpan todolist ke database
def save_todo(todolist):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for item in todolist:
            file.write(f"{item['tugas']}|{item['urgen']}|{item['deadline']}|{item['status']}")

# Load todolist dari database
def load_todo():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        data = []
        for line in file:
            parts = line.strip().split('|')
            if len(parts) == 4:
                tugas, urgen, deadline, status = parts
                data.append({
                    'tugas': tugas,
                    'urgen': urgen,
                    'deadline': deadline,
                    'status': status
                })
        return data

# Tampilkan To-Do List
def tampilkan_todo(todolist):
    while True:
        # Urutkan todolist, urgent di atas
        sorted_list = sorted(todolist, key=lambda x: x['urgen'] != "Urgent")

        if not sorted_list:
            print("> To-Do List Kosong")
        else:
            print("To-Do List:")
            for i, item in enumerate(sorted_list, start=1):
                print(f"[{i}] {item['tugas']} | {item['urgen']} | {item['deadline']} | {item['status']}")

        input("\nENTER untuk keluar")
        return

# Tambah Tugas
def tambah_tugas(todolist):
    while True:
        tugas = input("> Masukkan tugas baru: ").strip().capitalize()
        urgen = input("> Apakah tugas ini urgen? (Y/N): ").strip().capitalize()
        deadline = input("> Masukkan tenggat waktu (Tgl-Bln-Thn): ").strip().title()

        if urgen == "Y":
            urgen_label = "Urgent"
        elif urgen == "N":
            urgen_label = "Not urgent"
        else:
            urgen_label = urgen  # fallback jika input tidak sesuai

        if tugas and urgen and deadline:
            todolist.append({
                'tugas': tugas,
                'urgen': urgen_label,
                'deadline': deadline,
                'status': "Belum selesai"
            })
            save_todo(todolist)
            print("> Tugas berhasil ditambahkan :)")
        else:
            print("> Input tidak benar!")

        input("\nENTER untuk keluar")
        return

# Hapus Tugas
def hapus_tugas(todolist):
    while True:
        if not todolist:
            print("> Tugas kosong")
            input("\nENTER untuk keluar")
            return
        else:
            print("To-Do List:")
            for i, item in enumerate(todolist, start=1):
                print(f"[{i}] {item['tugas']} | {item['urgen']} | {item['deadline']} | {item['status']}")
        try:
            nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
            if 1 <= nomor <= len(todolist):
                tugas = todolist.pop(nomor - 1)
                save_todo(todolist)
                print(f"> Tugas '{tugas['tugas']}' berhasil dihapus.")
            else:
                raise ValueError
        except ValueError:
            print("> Nomor tugas tidak valid!")

        input("\nENTER untuk keluar")
        return

# Tandai tugas selesai
def tandai_selesai(todolist):
    while True:
        if not todolist:
            print("> To-Do List kosong")
            input("\nENTER untuk keluar")
            return
        else:
            print("To-Do List:")
            for i, item in enumerate(todolist, start=1):
                print(f"[{i}] {item['tugas']} | {item['urgen']} | {item['deadline']} | {item['status']}")
        try:
            nomor = int(input("Masukkan nomor tugas yang ingin ditandai selesai: "))
            if 1 <= nomor <= len(todolist):
                todolist[nomor - 1]['status'] = "Selesai"
                save_todo(todolist)
                print(f"> Tugas '{todolist[nomor - 1]['tugas']}' ditandai sebagai selesai.")
            else:
                raise ValueError
        except ValueError:
                print("> Masukkan nomor yang valid!")

        input("\nENTER untuk keluar")
        return

# Menu utama
def menu():
    todolist = load_todo()
    while True:
        print("<< Selamat Datang di To-Do List >>")
        print("Silakan pilih menu:")
        print("[1] Tampilkan To-Do List")
        print("[2] Tambah Tugas")
        print("[3] Hapus Tugas")
        print("[4] Tandai Tugas Selesai")
        print("[5] Tutup")

        pilihan = input("Pilih: ")

        if pilihan == "1":
            tampilkan_todo(todolist)
        elif pilihan == "2":
            tambah_tugas(todolist)
        elif pilihan == "3":
            hapus_tugas(todolist)
        elif pilihan == "4":
            tandai_selesai(todolist)
        elif pilihan == "5":
            print("<< Terima kasih telah menggunakan To-Do List :) >>")
            break
        else:
            print("> Pilihan tidak valid!, pilih yang benar! >:(")
            input("\nENTER untuk ulangi")

# Jalankan program
menu()