# by M. Ammar Hanif
from fractions import Fraction as fraction
# harus di revisi lagi, karena masih dirty code
# revisi:
# ----- variabel ngasal
# ----- semua belum menggunakan formatted string
# ----- terakhir, melakukan tes ulang

def menu():
    start()
    choice = input(" Selamat Datang \n Kalkulator Transformasi \n 1. Pencerminan \n 2. Translasi \n 3. Dilatasi \n 4. Rotasi \n 5. Rotasi dengan titik pusat selain (0,0) \n 0. Exit \n ")
    print()
    if choice == "1":
        Pencerminan()
        # masuk ke fungsi Pencerminan
    elif choice == "2":
        Translasi()
        # masuk ke fungsi Translasi
    elif choice == "3":
        Dilatasi()
        # masuk ke fungsi Dilatasi
    elif choice == "4":
        Rotasi()
        # masuk ke fungsi Rotasi
    elif choice == "5":
        rotasi_suatu_titik()
        # masuk ke fungsi rotasi suatu titik
    else:
        out()


def Pencerminan():
        start()
        choice = input(" Pilih Pencerminan \n 1. Terhadap sumbu X \n 2. Terhadap sumbu Y \n 3. Terhadap titik pusat \n 4. Terhadap garis Y=X \n 5. Terhadap garis Y=-X \n 6. Terhadap garis X = k \n 7. Terhadap garis Y = h \n 8. Back \n 0. Exit \n ")
        print()
        if choice == "1":
            terhadap_sb_x()
            # terhadap sumbu X
        elif choice == "2":
            terhadap_sb_y()
            # terhadap sumbu y
        elif choice == "3":
            zero()
            # terhadap titik pusat (0,0)
        elif choice == "4":
            terhadap_garis_y_smdengan_x()
            # terhadap garis Y = X
        elif choice == "5":
            terhadap_garis_y_smdengan_minusx()
            # terhadap garis Y = -X
        elif choice == "6":
            terhadap_garis_x_smdengan_k()
            # terhadap garis X = k (suatu angka)
        elif choice == "7":
            terhadap_garis_y_smdengan_h()
            # terhadap garis Y = h (suatu angka)
        elif choice == "8":
            Back()
        else:
            out()


def terhadap_sb_x():
        start()
        x_awal = input(' Masukan nilai awal variabel X \n = ')
        # input x awal
        print()
        y_awal = int(input(' Masukan nilai awal variabel Y \n = '))
        # input y awal
        print()
        y_hasil = -1 * int(y_awal)
        print(f" Hasil pencerminan = ({x_awal}, {y_hasil})")
        Pencerminan()


def terhadap_sb_y():
        start()
        x_awal = input(' Masukan nilai awal variabel x \n = ') 
        print()
        y_awal = input(' Masukan nilai awal variabel y \n = ')
        print()
        x_hasil = -1 * int(x_awal)
        print(f' Hasil pencerminan = ({x_hasil}, {y_awal})' )
        Pencerminan()


def zero():
        start()
        x_awal = input(' Masukan nilai awal variabel x \n = ')
        print()
        y_awal = input(' Masukan nilai awal variabel y \n = ')
        print()
        x_hasil = -1 * int(x_awal)
        y_hasil = -1 * int(y_awal)
        print(f' Hasil pencerminan = ({x_hasil}, {y_hasil})' )
        Pencerminan()


def terhadap_garis_y_smdengan_x():
        start()
        x_hasil = int(input(' Masukan nilai awal variabel x \n = '))
        print()
        y_hasil = int(input(' Masukan nilai awal variabel y \n = '))
        x_hasil, y_hasil = y_hasil, x_hasil
        print()
        print(f' Hasil pencerminan = ({x_hasil}, {y_hasil})')
        Pencerminan()


def terhadap_garis_y_smdengan_minusx():
    start()
    x_awal = input(' Masukan nilai awal variabel x \n = ')
    print()
    y_awal = input(' Masukan nilai awal variabel y \n = ')
    print()
    x_hasil = -1 * int(x_awal)
    y_hasil = -1 * int(y_awal)
    print()
    x_hasil, y_hasil = y_hasil, x_hasil
    print(f' Hasil pencerminan = ({x_hasil}, {y_hasil})' )
    Pencerminan()


def terhadap_garis_x_smdengan_k():
    start()
    var_x = int(input(' Masukan nilai garis X pada pencerminan \n X = '))
    # nilai garis X = k (suatu angka)
    print()
    x_awal = int(input(' Masukan nilai awal variabel x \n = '))
    print()
    y_awal = int(input(' Masukan nilai awal variabel y \n = '))
    print()
    x_hasil = (2 * int(var_x))-int(x_awal)
    print(f' Hasil pencerminan terhadap garis X = {var_x}, adalah: ({x_hasil}, {y_awal})' )
    Pencerminan()


def terhadap_garis_y_smdengan_h():
    start()
    var_y = int(input(' Masukan nilai garis Y pada pencerminan \n Y = ')) 
    # nilai garis Y = h (suatu angka)
    print()
    x_awal = int(input(' Masukan nilai awal variabel x \n = '))
    print()
    y_awal = int(input(' Masukan nilai awal variabel y \n = '))
    print()
    y_hasil = (2 * int(var_y)) - int(y_awal)
    print(f' Hasil pencerminan terhadap garis Y = {var_y}, adalah: ({x_awal}, {y_hasil})' )
    Pencerminan()


def Translasi():
    start()
    choice = input(' Pilihan Translasi \n 1. Translasi \n 2. Back \n 3. Exit \n ')
    print()
    if choice == "1":
        count_translasi()
        # hitung translasi
    elif choice == "2":
        Back()
    else:
        out()


def count_translasi():
    start()
    nilai_a = int(input(' Masukan nilai a Translasi (bagian atas) \n = '))
    print()
    nilai_b = int(input(' Masukan nilai b Translasi (bagian bawah) \n = '))
    print()
    x_awal = int(input(' Masukan nilai awal variabel x \n = '))
    print()
    y_awal = int(input(' Masukan nilai awal variabel y \n = '))
    print()
    x_hasil = int(nilai_a) + int(x_awal)  
    y_hasil = int(nilai_b) + int(y_awal) 
    print()
    print(f' Hasil Translasi T({nilai_a}, {nilai_b}), adalah: ({x_hasil}, {y_hasil})')
    Translasi()


def Dilatasi():
    print()
    print(' Loading ..... ')
    print()
    choice = input(' Pilihan Dilatasi \n 1. Dilatasi \n 2. Dilatasi dengan pusat selain (0,0) \n 3. Back \n 4. Exit \n ')
    print()
    if choice == "1":
        dilatasi_biasa()
    elif choice == "2":
        dilatasi_dengan_pusat_selain_nol()
    elif choice == "3":
        Back()
    else:
        out()


def dilatasi_biasa():
    start()
    skala_dilatasi = fraction(input(' Masukan nilai skala dilatasi (k) \n = '))
    print()
    x_awal = int(input(' Masukan nilai awal variabel x \n = '))
    print()
    y_awal = int(input(' Masukan nilai awal variabel y \n = '))
    print()
    x_hasil = skala_dilatasi * int(x_awal)
    y_hasil = skala_dilatasi * int(y_awal)
    print(f' Hasil Dilatasi terhadap skala = {skala_dilatasi}, adalah: ({fraction(x_hasil)}, {fraction(y_hasil)})')
    Dilatasi()


def dilatasi_dengan_pusat_selain_nol(): 
    start()
    skala_dilatasi = fraction(input(' Masukan nilai skala dilatasi (k) \n = '))
    print()
    titik_pusat_a = input(' Masukan nilai titik pusat a \n = ')
    print()
    titik_pusat_b = input(' Masukan nilai titik pusat b \n = ')
    print()
    x_awal = input(' Masukan nilai awal variabel x \n = ')
    print()
    y_awal = input(' Masukan nilai awal variabel y \n = ')
    print()
    x_hasil = skala_dilatasi * (int(x_awal) - int(titik_pusat_a)) + int(titik_pusat_a)
    y_hasil = skala_dilatasi * (int(y_awal) - int(titik_pusat_b)) + int(titik_pusat_b)
    print(f' Hasil Dilatasi terhadap skala = {skala_dilatasi}, dan titik pusat ({titik_pusat_a}, {titik_pusat_b}) adalah: \n ({fraction(x_hasil)}, {fraction(y_hasil)})' )
    Dilatasi()


def Rotasi():
    start()
    choice = input(' Pilih Rotasi \n 1. 90 derajat Searah Jarum Jam (-90 degree) \n 2. 90 derajat Berlawanan Arah Jarum Jam (90 degree) \n 3. 180 Derajat \n 4. 270 derajat Searah Jarum Jam (-270 degree) \n 5. 270 derajat Berlawanan Arah Jarum Jam (270 degree) \n 6. Back \n 7. Exit \n ')
    print()
    if choice == "1":
        searah_90_derajat_jarum_jam()
        # masuk ke fungsi rotasi -90 derajat
    elif choice == "2":
        berlawanan_90_derajat_jarum_jam()
        # masuk ke fungsi rotasi 90 derajat
    elif choice == "3":
        zero_1()
        # masuk ke fungsi rotasi +- 180 derajat
    elif choice == "4":
        berlawanan_90_derajat_jarum_jam()
        # karena -270 derajat = 90 derajat, maka masuk ke fungsi rotasi 90 derajat
    elif choice == '5':
        searah_90_derajat_jarum_jam()
        # karena 270 derajat = -90 derajat, maka masuk ke fungsi rotasi -90 derajat
    elif choice == "6":
        Back()
    else:
        out() 

def searah_90_derajat_jarum_jam():
    start()
    x_awal = int(input(" Masukan nilai awal variabel x: \n "))
    y_awal = int(input(" Masukan nilai awal variabel y: \n "))
    # x_hasil = int(y_awal) -------ini cara alternatif sebelumnya
    # y_hasil = -1 * int(x_awal) --------------------------------
    x_awal, y_awal = y_awal, x_awal
    y_hasil = -1 * int(y_awal)
    result = f'Hasil Rotasi -90 atau 270 derajat = ({x_awal},{y_hasil}) '
    print()
    print(result)
    Rotasi()

def berlawanan_90_derajat_jarum_jam():
    start()
    x_awal = int(input("Masukan nilai awal variabel x: \n "))
    y_awal = int(input("Masukan nilai awal variabel y: \n "))
    # x_hasil = -1 * y_awal #---ini cara sebelum di revisi
    # y_hasil = x #---------------------------------------
    x_awal, y_awal = y_awal, x_awal
    x_hasil = -1 * int(x_awal)
    result = f"Hasil Rotasi 90 atau -270 derajat = ({x_hasil}, {y_awal}) "
    print(result)
    Rotasi()

def zero_1():
    start()
    x_awal = int(input("Masukan nilai awal variabel x: \n "))
    y_awal = int(input("Masukan nilai awal variabel y: \n "))
    x_hasil = int(x_awal) * -1
    y_hasil = int(y_awal) * -1
    print(f'Hasil Rotasi 180 derajat = ({x_hasil}, {y_hasil}) ')
    Rotasi()

def rotasi_suatu_titik():
    start()
    # belom jadi boss, masih maintenance hahahahahha

def Back():
        print()
        print(' Loading ... ')
        print()
        menu()


def out():
        print()
        print(' Dankee... :)')
        print()


def start():
    print()
    print(" loading ... ")
    print()


menu()

