import random
print ("1. Gunting")
print ("2. Batu")
print("3. Kertas")

tipe = input ("Masukan Pilihan :")
if tipe in ("Gunting", "Batu", "Kertas"):
    choice = ("Gunting", "Batu", "Kertas")
    pilihan_random = random.choice (choice)
    print (pilihan_random)
    print (tipe, "Lawan", pilihan_random)

if tipe == pilihan_random :
    print ("Seri")
else :
    if tipe == 'Gunting':
        if pilihan_random == "Batu" :
            print ("Kalah")
            if pilihan_random == "kertas" :
                print ("Menang")
    elif tipe == 'Batu':
        if pilihan_random == "Kertas" :
            print ("Kalah")
            if pilihan_random == "Gunting" :
                print ("Menang")
    elif tipe == 'Kertas':
        if pilihan_random == "Gunting" :
            print ("Kalah")
            if pilihan_random == "Batu" :
                print ("Menang")
    else :
        print ("seri")