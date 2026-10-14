# 1. Input tinggi segitiga
tinggi_segitiga = int(input("Masukkan tinggi segitiga: "))

# 2. Perulangan luar untuk baris
for i in range(1, tinggi_segitiga +1):
    # 3. Perulangan dalam untuk mencetak bintang
    for j in range(i):
        print("*", end=" ")

    # 4. Pindah baris
    print() 