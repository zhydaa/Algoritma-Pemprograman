# Bubble Sort menggunakan Nested Loop
data = [10, 5, 40, 35, 20, 15, 30]
n = len(data)
print("Data sebelum diurutkan:", data)

# Outer loop untuk jumlah putaran (pass)
for i in range(n - 1):          
    # Inner loop untuk membandingkan elemen berdekatan 
    for j in range(n - 1 - i):    
        if data[j] > data[j + 1]:
            # Tukar posisi jika urutan salah
            data[j], data[j + 1] = data[j + 1], data[j]   
    print("Pass", i + 1, ":", data)

print("Data sesudah diurutkan:", data)