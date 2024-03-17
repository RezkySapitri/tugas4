a = float (input("Masukan angka untuk bilangan :"))

if a > 0 and a %2 == 1:
    print (f"{a} adalah bilangan positif dan ganjil ")
elif a > 0 and a %2 == 0:
    print (f"{a} adalah bilangan positif dan genap ")
elif a <  0 and a %2 == 1 :
    print (f"{a} adalah bilangan negatif  dan ganjil ")
elif a < 0 and a %2 == 0:
    print (f"{a} adalah bilangan negatif  dan genap ")
else :
    print (f"{a} adalah bilangan netral ")