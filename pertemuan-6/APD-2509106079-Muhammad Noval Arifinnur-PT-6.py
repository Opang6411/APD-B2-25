import os
userpw={
    'Noval':'079',
}
os.system('cls')
while True:
    print('--- Login ---')
    print('1. Login')
    print('2. Register')
    print('3. Keluar')
    pilihan=input('Masukkan pilihan anda: ')
    if pilihan=='1':
        print('--- Login ---')
        user=input('Masukkan username: ')
        psw=input('Masukkan password: ')
        if userpw.get(user)==psw:
            os.system('cls')
            while True:
                paket={'Paket A', 'Paket B', 'Paket C', 'Paket D','Paket E', 'Paket F', 'Paket G','Paket H','Paket I', 'Paket J', 'Paket K', 'Paket L'}
                print('Anda telah login')
                print('Selamat datang',user)
                print('Pilih menu yang ingin anda akses:')
                print('1. Lihat Paket')
                print('2. Tambahkan Paket')
                print('3. Hapus Paket')
                print('4. Update Paket')
                print('5. Keluar')
                menu=input('Masukkan pilihan anda: ')
                if menu=='1':
                    os.system('cls')
                    print('--- Lihat Paket ---')
                    print(paket)
                elif menu=='2':
                    os.system('cls')
                    print('--- Tambah Paket ---')
                    tambahpaket=input('Masukkan nama paket yang ingin ditambahkan: ')
                    paket.add(tambahpaket)
                    print(f'Paket {tambahpaket} telah ditambahkan')
                elif menu=='3':
                    os.system('cls')
                    print('--- Hapus Paket ---')
                    hapuspaket=input('Masukkan nama paket yang ingin dihapus: ')
                    paket.remove(hapuspaket)
                    print(f'Paket {paket} telah dihapus')
                elif menu=='4':
                    os.system('cls')
                    print('--- Update Paket ---')
                    updatepaket=input('Masukkan nama paket yang ingin diupdate: ')
                    if updatepaket in paket:
                        paket.remove(updatepaket)
                        newpaket=input('Masukkan nama paket baru: ')
                        paket.add(newpaket)
                        print(f'Paket {updatepaket} telah diupdate menjadi {newpaket}')
                    else:
                        print(f'Paket {updatepaket} tidak ditemukan')
                elif menu=='5':
                    os.system('cls')
                    print('Anda telah keluar')
                    break
                else:
                    os.system('cls')
                    print('Pilihan tidak tersedia')
        else:
            os.system('cls')
            print('Username atau password salah')
    elif pilihan=='2':
        print('--- Register ---')
        useradd=input('Masukkan username: ')
        pwdadd=input('Masukkan password: ')
        userpw[useradd]=pwdadd
        os.system('cls')
        print('Anda telah terdaftar')
    elif pilihan=='3':
        os.system('cls')
        print('Terima kasih telah menggunakan program ini')
        break
    else:
        os.system('cls')
        print('Sepertinya pilihan anda salah, silahkan coba lagi')