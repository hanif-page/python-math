#by M.A Hanif
import fractions
import math

def menu():
    choice = input('\n Kamu mau mencari apa ? \n 1. Hipotenusa segitiga \n 2. Tinggi segitiga \n 3. Alas segitiga \n 4. Luas Segitiga \n 5. Jenis Segitiga \n 6. Tripel pythagoras \n 7.Exit \n ')
    if choice == '1':
        hipotenusa()
    elif choice == '2':
        tinggi()
    elif choice == '3':
        alas()
    elif choice == '4':
        luas()
    elif choice == '5':
        tipe_segitiga()
    elif choice == '6':
        tripel()
    else:
        exit_out()

def hipotenusa():
     print()
     alas_segitiga = int(input(' Masukan nilai alas dari segitiga: '))
     print()
     tinggi_segitiga = int(input(' Masukan nilai tinggi dari segitiga: '))
     print()
     print( ' Sisi miring atau hipotenusa =' ,math.sqrt( alas_segitiga ** 2 + tinggi_segitiga ** 2) )
     menu()

def tinggi():
    print()
    hipotenusa_segitiga = int(input(' Masukan nilai hipotenusa dari segitiga: '))
    print()
    alas_segitiga = int(input(' Masukan nilai alas dari segitiga: '))
    print()
    print(  ' tinggi =', math.sqrt( hipotenusa_segitiga ** 2 - alas_segitiga ** 2) )
    menu()

def alas():
    print()
    hipotenusa_segitiga = int(input(' Masukan nilai hipotenusa dari segitiga: '))
    print()
    tinggi_segitiga = int(input(' Masukan nilai tinggi dari segitiga: '))
    print()
    print( ' alas =', math.sqrt( hipotenusa_segitiga ** 2 - tinggi_segitiga ** 2) )
    menu()

def luas():
    print()
    alas_segitiga = int(input(' Masukan nilai alas dari segitiga: '))
    print()
    tinggi_segitiga = int(input(' Masukan nilai tinggi dari segitiga: '))
    print()
    print( ' luas Segitiga =' ,alas_segitiga * tinggi_segitiga / 2)
    menu()

def tipe_segitiga():
    print()
    hipotenusa_segitiga = int(input(' Masukan nilai sisi miring (nilai tertinggi) \n ' ))
    print()
    alas_segitiga = int(input(' Masukan nilai alas \n '))
    print()
    tinggi_segitiga = int(input(' Masukan nilai tinggi \n '))

    if hipotenusa_segitiga ** 2 == alas_segitiga ** 2 + tinggi_segitiga ** 2:
      print()
      print(' Segitiga ini adalah segitiga siku-siku ')
      menu()

    elif hipotenusa_segitiga ** 2 < alas_segitiga ** 2 + tinggi_segitiga ** 2:
       print()
       print(' Segitiga ini adalah segitiga lancip ')
       menu()

    else:
       print()
       print(' Segitiga ini adalah segitiga tumpul ')
       menu()

def tripel():
    print()
    hipotenusa_segitiga = int(input(' Masukan nilai sisi miring (nilai tertinggi) \n '))
    tinggi_segitiga = int(input(' Masukan nilai tinggi \n '))
    alas_segitiga = int(input(' Masukan nilai alas \n '))

    if hipotenusa_segitiga ** 2 == alas_segitiga ** 2 + tinggi_segitiga ** 2:
        print()
        print(' Segitiga ini termasuk tripel pythagoras ')
        menu()

    else:
        print()
        print(' Segitiga ini tidak termasuk tripel pythagoras ')
        menu()

def exit_out():
    print('\n Terima Kasih \n')


menu()
