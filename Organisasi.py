
#print yang pas untuk program dibawah adalah 
Jenis_kelamin    = input("Masukan Jenis Kelamin Anda  :")
berat_badan      = float(input("Masukan Berat Badan Anda    :"))
Tinggi_Badan     = float(input("Masukan Tinggi Badan Anda   :"))
Usia             = float(input("Masukan Usia Anda           :"))
Skill            = input("Masukan Skill Anda (Jika tidak ada kosongkan):")
nilai_Akademis   = float(input("Masukan Nilai Akademis Anda :"))
cacat            = input("Apakah anda memiliki cacat anggota tubuh? (Ya/Tidak):").lower()
def kelayakan(Jenis_kelamin,berat_badan,Tinggi_Badan,Usia,Skill,nilai_Akademis,cacat):
    if Jenis_kelamin.lower() == 'perempuan':
        if  berat_badan >= 45 and berat_badan<= 50 and Tinggi_Badan >= 165 and Usia <= 20 and not cacat:
            return "Diterima"
        elif nilai_Akademis >= 90 and Usia <= 30 and not cacat:
             return "Diterima"
        elif Skill.lower () in ["menembak","memanah", "berkuda"] and not cacat:
            return "Diterima"
        elif cacat.lower() == "tidak":
            return "diterima"
        else :
            return "ditolak"
    elif Jenis_kelamin.lower() == 'laki-laki' :
        if berat_badan <= 70 and Tinggi_Badan >= 170 and Usia < 25 and not cacat :
            return "Diterima"
        elif nilai_Akademis >= 90 and Usia <= 30 and not cacat :
             return "Diterima"
        elif Skill.lower () in ["menembak","memanah", "berkuda"] and not cacat:
            return "Diterima"
        elif cacat.lower() == "tidak":
            return "diterima"
        else :
            return "ditolak "
    else :
        return "ditolak"
hasil_kelayakan =kelayakan(Jenis_kelamin,berat_badan,Tinggi_Badan,Usia,Skill,nilai_Akademis,cacat)
print ("kelayakan anda :", hasil_kelayakan)
