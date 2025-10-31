print ("===================================\n")

print("         Biodata Siswa       \n")

print ("===================================\n")

print("Nama\t: Rizqi maulana rifai ")
print("Nis\t: 123456789")
print("jurusan\t: RPL")
print("umur\t: 15")
print("hobi\t: bola")


Nama = "Ripaii"

if Nama is None:
    print("Nama belum diisi")
else:
    print("Nama kamu adalah",Nama)



list_1=[2,4,8,10]
print(list_1[0])

list_2=["grayson","jasan","tim","domain"]
print(list_2[2])

list_3=[24,False,"heloo pyton"]
print(list_3[1])

#Append
buah=["semangka","jeruk"]
buah.append("pisang")
print(buah)

#Extend
buah=["semangka","jeruk"]
buah.extend(["melon","manggis"])
print(buah)

#insert
angka=[1,2,3]
angka.insert(3,4)
print(angka)

#pop
buah=["apel","jeruk","mangga","pisang","kelengkeng","anggur"]
buah.pop(3)
print(buah)

#sort
angka=[5,2,9,1]
angka.sort()
print(angka)

angka=[5,2,9,1]
angka.sort(reverse=True)
print(angka)

#clear
data=[1,2,3]
data.clear()
print(data)

#remove
buah=["semangka","jeruk","mangga"]
buah.remove("semangka")
print(buah)

#index
nama=["rizqi","maulana","rifai"]
print(nama.index("maulana"))

#reverse
warna=["biru","kuning","hijau"]
buah.reverse()
print(warna)

#count
angka=[1,2,2,3,2,2,2,2,2]
print(angka.count(2))

#latihan

print("======== Biodata Siswa=======\n")

print("\nNo.1")
makanan=["beling","ayam tiren","paku"]
makanan.append("sesajen")
print(makanan)

print("\nNo.2")
makanan=["beling","ayam tiren","paku","linggis","sesajen"]
makanan.pop(3)
print(makanan)

print("\nNo.3")
makanan=["beling","ayam tiren","paku","linggis","sesajen"]
makanan.sort()
print(makanan)

print("\nNo.4")
makanan=["beling","ayam tiren","paku","linggis","sesajen"]
makanan.remove("linggis")
print(makanan)

print("\nNo.4")
makanan=["beling","ayam tiren","paku","linggis","sesajen"]
makanan.clear()
print(makanan)