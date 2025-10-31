#Membuat input data

#print("silahkan masukan nama anda:")
#nama = input()

#print(f"Hello {nama},salam kenal")

#tambahan
a = 1
b = 5

# Penjumlahan
hasil_tambah = a + b
print(f"{a} + {b} = {hasil_tambah}")

# Perkalian
hasil_kali = a * b
print(f"{a} * {b} = {hasil_kali}")

# Pembagian
hasil_bagi = a / b
print(f"{a} / {b} = {hasil_bagi}")

print("membuat bolean and")
print(True and True)
print(False and False)
print(True and False)
print(False and True)

print("membuat bolean or")
print(True or True)
print(False or False)
print(True or False)
print(False or True)

print("membuat bolean not")
print( not True)
print( not False)
print( not False)
print( not True)

print("membuat operator perbandingan")
# >lebih dari
# <kurang dari
# >=lebih dari sama dengan
# <=kurang dari sama  dengan
# ==sama dengan
# !=tidak sama dengan

print("nilai yang benar/true")
print(7>3)
print(1<4)
print(10>=3)
print(10<=18)
print(3==3)
print(5!=10)

print("nilai yang salah/false")
print(5>7)
print(22<3)
print(10>=28)
print(17<=10)
print(11==18)
print(8!=8)

print("latihan soal")
print("No.1 materi input-Buatlah yang menghasilkan pengguna memasukan nama,umur hobi,dan terakhir tampilan sapaan")
print("No.2 materi input number-buatlah program yang meminta pengguna memasukan umur,lalu menampil umur 2 tahun lagi")
print("No.3 materi Perbandingan-Buatlah program yang mengecek apakah umur sesoranng itu antara 10 sampai 17 tahun disebuat(remaja)")
print()
print("No.1")
nama = input("masukan nama:")
umur = input("masukan umur:")
hobi = input("masukan hobi:")

print(f"halo,nama saya {nama}, umur saya {umur} tahun,dan hobi saya adalah{hobi}.")

print()
print("No.2")
print("masukin umur")
umur = int(input())
tua = umur + 2
print(F"umur kamu {umur} dua tahun lagi kamu umur{tua}")

print()
print("No.3")

umur = int(input("masukan umur:"))
status = {True: "kamu adalah seorang remaja", False: "kamu bukan remaja,tumbuh lebih baik lagi ya!"}[(10 <= umur <= 17)]
print("status kamu:", status)








