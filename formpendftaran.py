print ("From pendaftaran untuk masuk universitas")

Nama            = input ("Masukan Nama Anda :")

Tempat_lahir    = input ("masukan tempat lahir anda :")
Tanggal_lahir   = int(input("masukan tanggal lahir anda :"))
Tahun_lahir     = int(input("masukan tahun lahir anda :"))
jenis_kelamin   = input ("Masukan jenis kelamin anda :")
 
Nilai_English       = float(input ("masukan nilai english anda :"))
Nilai_Mtk           = float (input("masukan nilai mtk anda :"))
Nilai_Indonesia     = float (input("masukan niali indonesia anda :"))

nilai_rata_rata  = (Nilai_English + Nilai_Mtk + Nilai_Indonesia)/3
if nilai_rata_rata >= 80 and jenis_kelamin.lower() == "Laki_laki":
    print ("Anda disarankan untuk masuk jurusan teknik informatika")
elif nilai_rata_rata >= 80 and jenis_kelamin.lower() == "Perempuan":
     print ("Anda disarankan untuk masuk jurusan sistem informasi")
else:
     print ("Anda disarankan masuk jurusan DKV")

umur = 2024 - Tahun_lahir

if umur > 25:
     print("Maaf anda tidak memenuhi persyaratan untuk diterima di universitas ini")