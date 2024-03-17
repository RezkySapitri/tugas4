a = float (input("Masukan bilangan pertama :"))
b = float (input("Masukukan bilangan kedua :"))
c = float (input("Masukan bilangan ketiga  :"))

if a < b and a < c  :
    print (f"bilangan {a} adalah bilangan terkecil")
elif b < a and b < c  :
    print (f"bilanagn {b} adalah bilangan terkecil ")
else :
    print (f"bilangan {c} adalah bilangan terkecil ")