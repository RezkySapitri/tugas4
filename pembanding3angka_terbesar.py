a = float (input("Masukan bilangan pertama :"))
b = float (input("Masukukan bilangan kedua :"))
c = float (input("Masukan bilangan ketiga  :"))

if a > b and a > c  :
    print (f"bilangan {a} adalah bilangan terbesar")
elif b > a and b > c  :
    print (f"bilanagn {b} adalah bilangan terbesar ")
elif c > a and c > b :
    print (f"bilangan {c} adalah bilangan terbesar ")
elif a == b and a > c and b > c :
    print (f"bilangan {a} sama dengan bilangan {b} dan lebih besar dari {c}")
elif a == c and a > b and c > b :
    print (f"bilangan {a} sama dengan bilangan {c} dan lebih besar dari {b}")
elif b == c and b > a and c > a :
    print (f"bilangan {b} sama dengan bilangan {c} dan lebih besar dari {a}")
else :
    print (f"semua bilangan tersebut sama besar")
