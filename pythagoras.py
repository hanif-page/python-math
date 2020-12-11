#by M.A Hanif
import fractions
def menu():
    print()
    choice = input(' Kamu mau mencari apa ? \n 1. Hipotenusa segitiga \n 2. Tinggi segitiga \n 3. Alas segitiga \n 4. Luas Segitiga \n 5. Jenis Segitiga \n 6. Tripel pythagoras \n 7. Exit \n ')
    if choice == '1':
        Hipotenusa()
    elif choice == '2':
        Tinggi()
    elif choice == '3':
        Alas()
    elif choice == '4':
        Luas()
    elif choice == '5':
        Type()
    elif choice == '6':
        Tripel()
    else:
        Exit()

def Hipotenusa():
     print()
     a = input(' Masukan nilai alas dari segitiga: ')
     print()
     t = input(' Masukan nilai tinggi dari segitiga: ')
     print()
     import math
     print( ' Sisi miring atau hipotenusa =' ,math.sqrt( int(a) ** 2 + int(t) ** 2) )
     menu()

def Tinggi():
    print()
    hipo = input(' Masukan nilai hipotenusa dari segitiga: ')
    print()
    a = input(' Masukan nilai alas dari segitiga: ')
    print()
    import math
    print(  ' Tinggi =' ,math.sqrt( int(hipo) ** 2 - int(a) ** 2) )
    menu()

def Alas():
    print()
    hipo = input(' Masukan nilai hipotenusa dari segitiga: ')
    print()
    t = input(' Masukan nilai tinggi dari segitiga: ')
    print()
    import math
    print( ' Alas =' ,math.sqrt( int(hipo) ** 2 - int(t) ** 2) )
    menu()

def Luas():
    print()
    a = input(' Masukan nilai alas dari segitiga: ')
    print()
    t = input(' Masukan nilai tinggi dari segitiga: ')
    print()
    print( ' Luas Segitiga =' ,int(a) * int(t) / 2)
    menu()

def Type():
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

def Tripel():
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


def Exit():
    print()
    print(' Terima Kasih ')

menu()
