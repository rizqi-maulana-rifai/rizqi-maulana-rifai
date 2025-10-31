#belajar elif

menu_pilihan =input("masukan pilihan menu (1/2/3):")

if menu_pilihan =="1":
    print("anda memilih menu 1")

elif menu_pilihan =="2":
    print("anda memilih menu 2")

elif menu_pilihan =="3":
    print("anda memilih menu 3")
else:
    print("menu tidak tersedia")





#1 buat kode masukan nilai

#nilai lebih besar sama dengan 90 nilainya A
#nilai lebih besar sama dengan 80 nilainya B
#nilai lebih besar sama dengan 70 nilainya C
#else nilai nya D

nilai = input ("masukan pilihan (90/80/70)= ")

if nilai >= "90":
    print("nilai anda A")

elif nilai >= "80":
    print("nilai anda B")

elif nilai >= "70":
    print("nilai anda C")

else:
    print("nilai anda D")

#no 2 buaqtkan masukan nilai suhu
#jika besar dari 35 suhunya panas banget
#jika besar dari 25 suhunya panas banget
#jika dibawah 25 suhunya panas banget

suhu = input ("masukan pilihan (35/25)= ")

if suhu >= "35":
    print("panass banget ")

elif suhu >= "25":
    print("hangatttt")

elif suhu <= "25":
    print("dinginnnnn")

else:
    print("dingin banget")

