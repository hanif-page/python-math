#by M.A Hanif
import fractions
import math

def menu():
    print()
    choice = input(' Kamu mau mencari apa ? \n 1. hipotenusa segitiga \n 2. tinggi segitiga \n 3. alas segitiga \n 4. luas Segitiga \n 5. Jenis Segitiga \n 6. tripel pythagoras \n 7. exit_out \n ')
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
     a = input(' Masukan nilai alas dari segitiga: ')
     print()
     t = input(' Masukan nilai tinggi dari segitiga: ')
     print()

     print( ' Sisi miring atau hipotenusa =' ,math.sqrt( int(a) ** 2 + int(t) ** 2) )
     menu()

def tinggi():
    print()
    hipo = input(' Masukan nilai hipotenusa dari segitiga: ')
    print()
    a = input(' Masukan nilai alas dari segitiga: ')
    print()
    print(  ' tinggi =' ,math.sqrt( int(hipo) ** 2 - int(a) ** 2) )
    menu()

def alas():
    print()
    hipo = input(' Masukan nilai hipotenusa dari segitiga: ')
    print()
    t = input(' Masukan nilai tinggi dari segitiga: ')
    print()
    print( ' alas =' ,math.sqrt( int(hipo) ** 2 - int(t) ** 2) )
    menu()

def luas():
    print()
    a = input(' Masukan nilai alas dari segitiga: ')
    print()
    t = input(' Masukan nilai tinggi dari segitiga: ')
    print()
    print( ' luas Segitiga =' ,int(a) * int(t) / 2)
    menu()

def tipe_segitiga():
    print()
    hipo = input(' Masukan nilai sisi miring (nilai tertinggi) \n ' )
    print()
    a = input(' Masukan nilai alas \n ')
    print()
    t = input(' Masukan nilai tinggi \n ')

    if int(hipo) ** 2 == int(a) ** 2 + int(t) ** 2:
      print()
      print(' Segitiga ini adalah segitiga siku-siku ')
      menu()

    elif  int(hipo) ** 2 < int(a) ** 2 + int(t) ** 2:
       print()
       print(' Segitiga ini adalah segitiga lancip ')
       menu()

    else:
       print()
       print(' Segitiga ini adalah segitiga tumpul ')
       menu()

def tripel():
    print()
    hipo = input(' Masukan nilai sisi miring (nilai tertinggi) \n ')
    t = input(' Masukan nilai tinggi \n ')
    a = input(' Masukan nilai alas \n ')

    if int(hipo) ** 2 == int(a) ** 2 + int(t) ** 2:
        print()
        print(' Segitiga ini termasuk tripel pythagoras ')
        menu()

    else:
        print()
        print(' Segitiga ini tidak termasuk tripel pythagoras ')
        menu()


def exit_out():
    print()
    print(' Terima Kasih ')

menu()
