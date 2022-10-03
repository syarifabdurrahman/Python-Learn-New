books_total= 10
print(f"Jumlah total buku {books_total}")
print('Ibu berkata, "baca bukumu!"')
books_total_readed = 0

# For loop
for i in range(0,books_total):
    if books_total_readed != books_total:
        books_total_readed += 1
        print(f'anak membaca buku ke {books_total_readed}')
    
if books_total_readed == books_total:
    print("Buku sudah dibaca semua")


# While
while books_total_readed < books_total:
    books_total_readed += 1
    print(f"Baca 1 buku yang belum dibaca. buku ke {books_total_readed}")

if books_total_readed == books_total:
    print("Buku sudah dibaca semua")

