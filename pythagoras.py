#by M.A Hanif
import math

def welcome(name):
    print(f'==========================================')
    print(f'=========Selamat Datang {name}============')
    print(f'==========================================')
    print('program ini dibuat untuk membantu menyelesaikan masalah tentang sisi segitiga')

def menu(name):
    choice = int(input(f'\n {name} mau mencari apa ? \n 1. Hipotenusa segitiga \n 2. Tinggi segitiga \n 3. Alas segitiga \n 4. Luas Segitiga \n 5. Jenis Segitiga \n 6. Tripel pythagoras \n 7. Exit \n '))
    if choice == 1:
        hipotenusa()
        # masuk ke fungsi hipotenusa
    elif choice == 2:
        tinggi()
        # masuk ke fungsi tinggi
    elif choice == 3:
        alas()
        # masuk ke fungsi alas
    elif choice == 4:
        luas()
        # masuk ke fungsi luas
    elif choice == 5:
        tipe_segitiga()
        # masuk ke fungsi tipe_segitiga
    elif choice == 6:
        tripel()
        # masuk ke fungsi tripel
    else:
        exit_out(name)
        # masuk ke fungsi exit_out

def hipotenusa(): 
    # fungsi ini berguna untuk menghitung besar sisi miring sebuah segitiga
     print()
     alas_segitiga = int(input('Masukan nilai alas dari segitiga: ')) # meminta nilai alas dari segitiga
     print()
     tinggi_segitiga = int(input('Masukan nilai tinggi dari segitiga: ')) # meminta nilai tinggi dari segitiga
     print()
     print(f'Sisi miring atau hipotenusa = {round(math.sqrt( alas_segitiga ** 2 + tinggi_segitiga ** 2))}') #di baris ini, gw tambahin round, buat iseng aja sbnrnya klo emg hasilnya koma wkwk
     menu(name)

def tinggi():
    # fungsi ini berguna untuk menghitung besar sisi tinggi sebuah segitiga
    print()
    hipotenusa_segitiga = int(input('Masukan nilai hipotenusa dari segitiga: ')) # meminta nilai hipotenusa/sisi miring dari segitiga
    print()
    alas_segitiga = int(input('Masukan nilai alas dari segitiga: ')) # meminta nilai alas dari segitiga
    print()
    print(f'tinggi = {math.sqrt( hipotenusa_segitiga ** 2 - alas_segitiga ** 2)}') 
    menu(name)

def alas():
    # fungsi ini berguna untuk menghitung besar sisi alas sebuah segitiga
    print()
    hipotenusa_segitiga = int(input('Masukan nilai hipotenusa dari segitiga: ')) # meminta nilai hipotenusa/sisi miring dari segitiga
    print()
    tinggi_segitiga = int(input('Masukan nilai tinggi dari segitiga: ')) # meminta nilai tinggi dari segitiga
    print()
    print(f'alas = {math.sqrt( hipotenusa_segitiga ** 2 - tinggi_segitiga ** 2)}')
    menu(name)

def luas():
    # fungsi ini berguna untuk menghitung luas sebuah segitiga
    print()
    alas_segitiga = int(input('Masukan nilai alas dari segitiga: ')) # meminta nilai alas dari segitiga
    print()
    tinggi_segitiga = int(input('Masukan nilai tinggi dari segitiga: ')) # meminta nilai tinggi dari segitiga
    print()
    print(f'luas Segitiga = {alas_segitiga * tinggi_segitiga / 2}')
    menu(name)

def tipe_segitiga():
    # fungsi ini berguna untuk menentukan jenis segitiga dari sisi-sisinya
    print()
    hipotenusa_segitiga = int(input('Masukan nilai sisi miring (nilai tertinggi) \n ')) # meminta nilai hipotenusa/sisi miring dari segitiga
    print()
    alas_segitiga = int(input('Masukan nilai alas \n ')) # meminta nilai alas dari segitiga
    print()
    tinggi_segitiga = int(input('Masukan nilai tinggi \n ')) # meminta nilai tinggi dari segitiga

    if hipotenusa_segitiga ** 2 == alas_segitiga ** 2 + tinggi_segitiga ** 2:
      print()
      print(f'Segitiga ini adalah segitiga siku-siku ')
      menu(name)

    elif hipotenusa_segitiga ** 2 < alas_segitiga ** 2 + tinggi_segitiga ** 2:
       print()
       print(f'Segitiga ini adalah segitiga lancip ')
       menu(name)

    else:
       print()
       print(f'Segitiga ini adalah segitiga tumpul ')
       menu(name)

def tripel():
    # fungsi ini berguna untuk menentukan apakah suatu segitiga itu tripel pythagoras atau tidak dari sisi-sisinya
    print()
    hipotenusa_segitiga = int(input('Masukan nilai sisi miring (nilai tertinggi) \n ')) # meminta nilai hipotenusa/sisi miring dari segitiga
    tinggi_segitiga = int(input('Masukan nilai tinggi \n ')) # meminta nilai tinggi dari segitiga
    alas_segitiga = int(input('Masukan nilai alas \n ')) # meminta nilai alas dari segitiga

    if hipotenusa_segitiga ** 2 == alas_segitiga ** 2 + tinggi_segitiga ** 2:
        print()
        print(f'Segitiga ini termasuk tripel pythagoras ')
        menu(name)

    else:
        print()
        print(f'Segitiga ini tidak termasuk tripel pythagoras ')
        menu(name)

def exit_out(name):
    # fungsi keluar dari program
    print(f'\n Terima Kasih {name} \n')

name = input('Masukan nama kamu: ')
welcome(name)
menu(name)
