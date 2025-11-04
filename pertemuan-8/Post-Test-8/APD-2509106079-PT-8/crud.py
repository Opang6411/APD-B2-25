pengguna = {'Noval': '079'}
paket = ['Paket A', 'Paket B', 'Paket C', 'Paket D','Paket E','Paket F','Paket G','Paket H']
program_berjalan=True
import os
from prettytable import PrettyTable
def bersihin():
    os.system('cls')

def menu_paket():
    while True:
        print('\n-- PAKET MENU --')
        print('1. Lihat Paket')
        print('2. Tambah Paket')
        print('3. Update Paket')
        print('4. Hapus Paket')
        print('5. Kembali')
        c = input('Pilih (1-5): ')
        if c == '1':
            bersihin()
            print('Daftar paket:')
            table = PrettyTable()
            table.field_names = ["No", "Nama Paket"]
            for i, p in enumerate(paket, 1):
                table.add_row([i, p])
            print(table)
        elif c == '2':
            print('Daftar paket:')
            table = PrettyTable()
            table.field_names = ["No", "Nama Paket"]
            for i, p in enumerate(paket, 1):
                table.add_row([i, p])
            print(table)
            tambah_paket()            
        elif c == '3':
            print('Daftar paket:')
            table = PrettyTable()
            table.field_names = ["No", "Nama Paket"]
            for i, p in enumerate(paket, 1):
                table.add_row([i, p])
            print(table)
            lama = input('Nama paket yang diupdate: ')
            baru = input('Nama paket baru: ')
            if ubah_paket(lama, baru):
                print('Paket berhasil diupdate')
            else:
                print('Gagal update paket')
        elif c == '4':
            print('Daftar paket:')
            table = PrettyTable()
            table.field_names = ["No", "Nama Paket"]
            for i, p in enumerate(paket, 1):
                table.add_row([i, p])
            print(table)
            hapus_paket()
        elif c == '5':
            return
        else:
            print('Pilihan tidak valid')

def tambah_paket():
    tambah = input('Nama paket baru: ')
    if not tambah:
        print('Nama kosong')
        return
    if tambah in paket:
        print('Sudah ada')
    else:
        paket.append(tambah)
        print('Ditambahkan:', tambah)

def ubah_paket(lama, baru):
    if lama in paket and baru:
        idx = paket.index(lama)
        paket[idx] = baru
        return True
    return False

def hapus_paket():
    hapus = input('Nama paket hapus: ')
    if hapus in paket:
        paket.remove(hapus)
        print('Dihapus:', hapus)
    else:
        print('Tidak ditemukan')