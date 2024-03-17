def questioner():
    jenis_kelamin = input("Jenis kelamin (laki-laki/perempuan): ").lower()
    berat_badan = float(input("Berat badan (kg): "))
    tinggi = float(input("Tinggi badan (cm): "))
    usia = int(input("Usia: "))
    nilai_akademis = float(input("Nilai akademis : "))
    skill = input("Apakah memiliki skill (menembak/memanah/berkuda) (jika ada, jika tidak isi dengan 'tidak'): ").lower()
    cacat_anggota_tubuh = input("Apakah memiliki cacat anggota tubuh (ya/tidak): ").lower()
def cek_kelayakan(jenis_kelamin, berat_badan, tinggi, usia, nilai_akademis,skill, cacat_anggota_tubuh):
    if cacat_anggota_tubuh:
        return "Diterima"
    elif jenis_kelamin == "perempuan" and berat_badan >= 45 and berat_badan <= 50 and tinggi >= 165 and usia < 20:
            return "Diterima"
    elif jenis_kelamin == "laki-laki" and usia <= 25 and berat_badan <= 70 and tinggi >= 170:
         return "Diterima"
    elif nilai_akademis >= 90:
        return "Diterima"
    elif skill in ["menembak", "memanah", "berkuda"]:
        return "Diterima"
    else :
         return "Ditolak"
    
if questioner():
    print("Anda lulus dalam organisasi X!")
else:
    print("Maaf, Anda tidak memenuhi kriteria untuk lulus dalam organisasi X.")
