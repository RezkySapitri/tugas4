Algoritma           = float(input("Masikan Nilai Algoritma Anda :"))
Perancangan_Objek   = float(input("Masukan Nilai Perancang Objek Anda :"))
Kalkulus            = float(input("Masikan Nilai Kalkulus Anda :"))
Etika_Profrsi       = float(input("Masikan Nilai Etika Profesi Anda :"))
Database            = float(input("Masikan Nilai Database Anda :"))
English1            = float(input("Masikan Nilai English Anda :"))

def nilaiToBobot (nilai)  :
    if nilai >= 90 :
        return 4
    elif nilai >= 85 :
        return 3.75
    elif nilai >= 80 :
        return 3.5
    elif nilai >= 75:
        return 3.25
    elif nilai >= 70:
        return 3
    elif nilai >= 65:
        return 2.75
    elif nilai >= 60:
        return 2.5
    elif nilai >= 55: 
        return 2.25
    else :
        return 2.0
    
sks_algoritma = 3
sks_objek = 3
sks_etika = 2
sks_kalkulus = 4
sks_database = 3
sks_english1 = 2

total_algoritma = sks_algoritma * nilaiToBobot(Algoritma)
total_objek = sks_etika * nilaiToBobot(Perancangan_Objek)
total_etika = sks_objek * nilaiToBobot(Etika_Profrsi)
total_kalkulus = sks_kalkulus * nilaiToBobot(Kalkulus)
total_database = sks_database * nilaiToBobot(Database)
total_english1 = sks_english1 * nilaiToBobot(English1)

total_sks =sks_algoritma + sks_objek + sks_etika + sks_kalkulus + sks_database + sks_english1

IPK = (total_algoritma + total_objek + total_etika + total_kalkulus + total_database + total_english1) / total_sks

print ("Total sks anda adalah :", total_sks)
print ("IPk anda adalah : ", IPK)



