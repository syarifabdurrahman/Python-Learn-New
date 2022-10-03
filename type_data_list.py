daftar_buku=['Dragon ball','Seven habbits','First Thing First']
print('Tampilkan variable daftar_buku')
print(daftar_buku)

print('\nProses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan indeks buku tertentu')
print(daftar_buku[0])
print(daftar_buku[1])

print('\nTampilkan buku dengan for in range')
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])


daftar_buku=[1,'Rurouni kenshin',-332,3.14]
print('\nTampilkan buku denagn for in range dengan tipe data berbeda beda')
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar_buku')
daftar_buku=['Dragon ball','Seven habbits','First Thing First']
print('Tambahkan 1 buku baru menggunakan "append"')
daftar_buku.append('Bleach')
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku=['Dragon ball','Seven habbits','First Thing First']
print("\nclear list")
daftar_buku.clear()
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti elemen pertama dari list')
daftar_buku=['Dragon ball','Seven habbits','First Thing First','Naruto','Digimon']
daftar_buku[0]='Samurai'
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMengambil dan disimpan divariable element ke-n pada list')
buku = daftar_buku.pop(2)
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nbuku yang diambil')
print(buku)

daftar_buku.pop() ## dari ujung list
daftar_buku.pop(-1) ## mengambil 1 dari ujung list