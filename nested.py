#max = int(input("jumlah bintang:"))
#for i in range(max):
 #   for j in range(0,
  #   max - i):
   #     print("*", end=" ")       
#    print()    



#max = int(input("jumlah bintang:"))
#for i in range(max):
 #   for j in range(i):
  #      print(" ", end="*")
   # print()



#belajar berhitung
a = int(input("masukan angka pertama: "))
b = int(input("masukan angka kedua: "))
operator = input("masukan operator(=,-,*,/): ")

match operator:
    case "+":
        hasil = a + b
        print(f"hasildari{a} + {b} = {hasil}")
    case "-":
        hasil = a - b
        print(f"hasildari{a} - {b} = {hasil}")
    case "*":
        hasil = a * b
        print(f"hasildari{a} * {b} = {hasil}")
    case "/":
        if b !=0:
            hasil = a / b
            print(f"hasildari{a} / {b} = {hasil}")
        else:
            print("eror: pembagian dengan nol tidak bisa")    
    case _:
        print("operator tidak dikenal!")
    



