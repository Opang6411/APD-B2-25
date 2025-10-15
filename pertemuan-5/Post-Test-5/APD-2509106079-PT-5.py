import os

username=["Noval"]
password=["079"]
listbrg=[['Paket A','Paket B','Paket C'],['Paket D','Paket E','Paket F'],['Paket G','Paket H','Paket I']]
while True:
    print("Selamat Datang di Sistem Kurir")
    print("Silahkan Login Terlebih Dahulu")
    print("(Ketik Enter pada Username dan Password untuk keluar)")
    user=input("Masukkan Nama Pengguna: ")
    pwd=input("Masukkan Password Pengguna: ")
    if user in username:
        idx=username.index(user)
        if pwd==password[idx]:
            while True:
                print("Jalan AWS")
                print(listbrg[0])
                print("Jalan Juanda")
                print(listbrg[1])
                print("Jalan MT Haryono")
                print(listbrg[2])
                print("1. Tambah Barang")
                print("2. Hapus Barang")
                print("3. Keluar")
                input_tindakan=input("Pilih Tindakan yang diinginkan: ")
                if input_tindakan=='1':
                    lokasi=int(input("Masukkan Lokasi (0-2): "))
                    barang=input("Masukkan Nama Barang: ")
                    listbrg[lokasi].append(barang)
                    print("Barang berhasil ditambahkan")
                elif input_tindakan=='2':
                    lokasi=int(input("Masukkan Lokasi (0-2): "))
                    barang=input("Masukkan Nama Barang: ")
                    if barang in listbrg[lokasi]:
                        listbrg[lokasi].remove(barang)
                        print("Barang berhasil dihapus")
                    else:
                        print("Barang tidak ditemukan")
                elif input_tindakan=='3':
                    print("Keluar dari program")
                    break
                else:
                    print("Tindakan tidak valid")  
                os.system('cls')
        else:
            print("Password salah")
    elif user=="" and pwd=="":
        print("Terima kasih telah menggunakan sistem kami")
        break
    else:
        print("Nama pengguna tidak ditemukan")
        input_daftar=input("Apakah Anda ingin mendaftar? (ya/tidak): ")

        if input_daftar=='ya':
            new_user=input("Masukkan Nama Pengguna Baru: ")
            new_pwd=input("Masukkan Password Baru: ")
            username.append(new_user)
            password.append(new_pwd)
            print("Pendaftaran berhasil, silahkan login kembali")
        else:
            print("Silahkan coba login kembali")
        os.system('cls')
os.system('cls')