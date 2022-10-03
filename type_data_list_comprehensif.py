# daftar_buku=['Dragon ball','Seven habbits','First Thing First','Naruto','Digimon']
# del daftar_buku [0:-2] ## [start : stop]
# for i in range (0, len(daftar_buku)):
#     print(daftar_buku[i])

# daftar_buku=['Dragon ball','Seven habbits','First Thing First','Naruto','Digimon']
# del daftar_buku [0::3] ## [start : stop : step]
# for i in range (0, len(daftar_buku)):
#     print(daftar_buku[i])

# print("\nmembuat list baru")
# daftar_buku=['Dragon ball','Seven habbits','First Thing First','Naruto','Digimon']
# daftar_buku_new = daftar_buku[:]


# print("\nMenghapus")
# del daftar_buku [:]
# for i in range (0, len(daftar_buku)):
#     print(daftar_buku[i])

# print("\nMenampilkan data semula")   
# for i in range (0, len(daftar_buku_new)):
#     print(daftar_buku_new[i])

print("\nMembuat list baru list comperehension: ganjil")
daftar_buku=['1. Dragon ball','2. Seven habbits','3. First Thing First','4. Naruto','5. Digimon']
daftar_buku_new= daftar_buku [0::2]
for i in range (0, len(daftar_buku_new)):
    print(daftar_buku_new[i])


print("\nMembuat list baru list comperehension: genap")
daftar_buku=['1. Dragon ball','2. Seven habbits','3. First Thing First','4. Naruto','5. Digimon']
daftar_buku_new= daftar_buku [1::2]
for i in range (0, len(daftar_buku_new)):
    print(daftar_buku_new[i])
