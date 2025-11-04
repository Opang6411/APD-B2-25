
pengguna = {'Noval': '079'}
paket = ['Paket A', 'Paket B', 'Paket C', 'Paket D','Paket E','Paket F','Paket G','Paket H']
program_berjalan=True
import os
def bersihin():
    os.system('cls')


from login import menu
from crud import menu_paket

try:
    while program_berjalan:
        hasil = menu()
        if hasil == 'exit':
            print('Keluar...')
            program_berjalan = False
            break
        elif hasil:
            menu_paket()
except KeyboardInterrupt:
    print('\nProgram dihentikan')