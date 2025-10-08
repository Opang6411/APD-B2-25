nama="Muhammad Noval Arifinnur"
password="2509106079"

coba=0
while coba<3 :


    inputnama=input("Masukkan ID anda : ")
    inputpass=input("Masukkan Password anda : ")
    if inputnama==nama and inputpass==password:
        jumlahbeli=0
        jmlbljr = 0
        jmlrak = 0
        jmlsofa = 0

        while True:
            sofa=500000
            mejabljr=250000
            raklmri=150000
            print("\n=== Menu Pembelian Furnitur===")
            print("1. Sofa Rp.500000")
            print("2. Meja Belajar Rp.250000")
            print("3. Rak Lemari Rp.150000")
            print("4. Keluar")
            belibrg=input("Masukkan barang yang ingin anda beli: ")
            if belibrg=="1":
                jmlsofa=int(input("Masukkan jumlah barang yang ingin dibeli: "))
                jumlahbeli+=sofa*jmlsofa
            elif belibrg=="2":
                jmlbljr=int(input("Masukkan jumlah barang yang ingin dibeli: "))
                jumlahbeli+=mejabljr*jmlbljr
            elif belibrg=="3":
                jmlrak=int(input("Masukkan jumlah barang yang ingin dibeli: "))
                jumlahbeli+=raklmri*jmlrak
            elif belibrg=="4":
                break
            else:
                print("Maaf input error")
        
        if jumlahbeli>=700000:
            jumlahbeli-=jumlahbeli*20/100
            print("\n=== Struk Pembelian Furnitur Infordeh===")
            print("Total sofa yang dibeli:",jmlsofa)
            print("Total meja belajar yang dibeli:",jmlbljr)
            print("Total rak lemari yang dibeli:",jmlrak)
            print("Selamat anda mendapat diskon sebesar 20%")
            print("Total pembayaran anda menjadi : Rp. ",int(jumlahbeli))
        elif jumlahbeli >= 500000 and jumlahbeli<700000:
            jumlahbeli-=jumlahbeli*8/100
            print("\n=== Struk Pembelian Furnitur Infordeh===")
            print("Total sofa yang dibeli:",jmlsofa)
            print("Total meja belajar yang dibeli:",jmlbljr)
            print("Total rak lemari yang dibeli:",jmlrak)
            print("Selamat anda mendapat diskon sebesar 8%")
            print("Total pembayaran anda menjadi : Rp. ",int(jumlahbeli))
        elif jumlahbeli>=150000 and jumlahbeli <500000:
            print("\n=== Struk Pembelian Furnitur Infordeh===")
            print("Total sofa yang dibeli:",jmlsofa)
            print("Total meja belajar yang dibeli:",jmlbljr)
            print("Total rak lemari yang dibeli:",jmlrak)
            print("Selamat anda mendapat kitchen set")
            print("Total pembayaran anda adalah : Rp. ",int(jumlahbeli))
        elif jumlahbeli>=0:
            print("\n=== Struk Pembelian Furnitur Infordeh===")
            print("Total sofa yang dibeli:",jmlsofa)
            print("Total meja belajar yang dibeli:",jmlbljr)
            print("Total rak lemari yang dibeli:",jmlrak)
            print("Total pembayaran anda adalah : Rp. ",int(jumlahbeli))
        else:
            print("Sepertinya ada error")
        break
    else:
        print("Gagal login")
        coba+=1
else :print("Maaf anda tidak bisa login lagi")