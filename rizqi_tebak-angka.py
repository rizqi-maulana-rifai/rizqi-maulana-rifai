import random

def tebak_angka():
    print("Selamat datang di game Tebak Angka!")
    print("Saya telah memilih angka antara 1 dan 100. Coba tebak angka tersebut.")
    
    # Komputer memilih angka acak antara 1 dan 100
    angka_rahasia = random.randint(1, 100)
    tebakan = None
    jumlah_tebakan = 0
    
    # Pemain menebak hingga angka yang benar ditemukan
    while tebakan != angka_rahasia:
        try:
            tebakan = int(input("Masukkan tebakan Anda: "))
            jumlah_tebakan += 1
            if tebakan < angka_rahasia:
                print("Terlalu rendah. Coba lagi!")
            elif tebakan > angka_rahasia:
                print("Terlalu tinggi. Coba lagi!")
        except ValueError:
            print("Masukkan angka yang valid!")
    
    print(f"Selamat! Anda berhasil menebak angka {angka_rahasia} setelah {jumlah_tebakan} percobaan.")

# Menjalankan game
tebak_angka()
