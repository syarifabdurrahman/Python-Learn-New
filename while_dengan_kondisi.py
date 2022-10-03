books_total= 10
print(f"Jumlah total buku {books_total}")
print('Ibu berkata, "baca bukumu!, pahami juga"')
books_total_readed= 0
books_readed_and_understand= 0

#While 
while books_total_readed < books_total * 2:
    books_total_readed+=1
    if books_readed_and_understand == 9:
        print(f"Buku ke {books_readed_and_understand + 1}, belum paham")
    else:
        books_readed_and_understand+=1
        print(f"Buku ke {books_readed_and_understand}, sudah dibaca dan dipahami")

if books_readed_and_understand == books_total:
    print("semua buku sudah dibaca dan dipahami")
else:
    print(f"tidak semua buku bisa dipahami, hanya {books_readed_and_understand} yang bisa dipahami")