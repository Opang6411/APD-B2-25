pengguna = {'Noval': '079'}
paket = ['Paket A', 'Paket B', 'Paket C', 'Paket D','Paket E','Paket F','Paket G','Paket H']
program_berjalan=True
import os
def bersihin():
    os.system('cls')

def daftar_pengguna(u, p):
    if not u or not p:
        return False
    if u in pengguna:
        return False
    pengguna[u] = p
    return True

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
        

def cek_login(u, p):   
    return pengguna.get(u) == p