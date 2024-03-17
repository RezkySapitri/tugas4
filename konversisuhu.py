celcius =float (input("Masukan nilai celcius :"))
fahrenheit = float (input("Masukan nilai Fahrenheit :"))

Celcius  = ( fahrenheit -32 )* 5/9 
Fahrenheit = (celcius * 9/5) +32
pilihan_konversi = input ("Masukan pilihan :")
print ("Pilih konversi :")
print (" 1. celcius ke fahrenheit :", Fahrenheit)
print (" 2. fahrenheit ke celcius :", Celcius)


if pilihan_konversi == '1' :
    print ("suhu dalam fahrenheit   ",Fahrenheit )
elif pilihan_konversi == '2' :
    print ("Suhu dalam celcius  ",Celcius)
else :
    print ("pilihan tidak valid. Silahkan pilih 1 atau 2")
