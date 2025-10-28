import os

pengguna = {'Noval': '079'}
paket = ['Paket A', 'Paket B', 'Paket C', 'Paket D','Paket E','Paket F','Paket G','Paket H']
program_berjalan=True

def bersihin():
    os.system('cls')

def lihat_paket():
    for p in paket:
        print('-', p)

def daftar_pengguna(u, p):
    if not u or not p:
        return False
    if u in pengguna:
        return False
    pengguna[u] = p
    return True

def cek_login(u, p):   
    return pengguna.get(u) == p

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

def hapus_paket():
    hapus = input('Nama paket hapus: ')
    if hapus in paket:
        paket.remove(hapus)
        print('Dihapus:', hapus)
    else:
        print('Tidak ditemukan')

def ubah_paket(lama, baru):
    if lama in paket and baru:
        idx = paket.index(lama)
        paket[idx] = baru
        return True
    return False

def menu():
    while True:
        print('\n-- MENU UTAMA --')
        print('1. Login')
        print('2. Register')
        print('3. Keluar')
        c = input('Pilih (1-3): ')
        if c == '1':
            username = input('Username: ')
            password = input('Password: ')
            if cek_login(username, password):
                bersihin()
                print('Berhasil login sebagai', username)
                return username
            else:
                print('Login gagal')
        elif c == '2':
            new_user = input('Username baru: ')
            new_pass = input('Password baru: ')
            if not new_user or not new_pass:
                print('Username/password tidak boleh kosong')
            elif daftar_pengguna(new_user, new_pass):
                print('Registrasi berhasil')
            else:
                print('Registrasi gagal: username sudah ada')
        elif c == '3':
            return 'exit'
        else:
            print('Pilihan tidak valid')
        bersihin()


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
            for p in (paket):
                print('-', p)
        elif c == '2':
            print('Daftar paket:')
            for p in (paket):
                print('-', p)
            tambah_paket()            
        elif c == '3':
            print('Daftar paket:')
            for p in paket:
                print('-', p)
            lama = input('Nama paket yang diupdate: ')
            baru = input('Nama paket baru: ')
            if ubah_paket(lama, baru):
                print('Paket berhasil diupdate')
            else:
                print('Gagal update paket')
        elif c == '4':
            print('Daftar paket:')
            for p in paket:
                print('-', p)
            hapus_paket()
        elif c == '5':
            return
        else:
            print('Pilihan tidak valid')

try:
    while program_berjalan:
        hasil = menu()
        if hasil == 'exit':
            print('Keluar...')
            program_berjalan = False
            break
        elif hasil:
            # panggil paket menu (tidak butuh argumen di versi sederhana ini)
            menu_paket()
except KeyboardInterrupt:
    print('\nProgram dihentikan')