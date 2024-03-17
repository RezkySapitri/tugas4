import math
a = float (input("Masukan angka untuk sisi a :"))
b = float (input("Masukan angka untuk sisi b :"))
c = float (input("Masukan angka untuk sisi c :"))

s = (a+b+c)/2
L = math.sqrt (s*(s - a)*(s-b)*(s-c))
K = a + b + c 

print ("semi-parimeter adalah ", s)
print ("Luas segitiga adalah", L)
print ("keliling segitiga adalah", K)