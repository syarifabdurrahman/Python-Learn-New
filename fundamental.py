# Sekuinsial : langkah berurutan
# print('Ibu berkata, "Pergi ke toko"')
# print('Budi menjawab, "Oke, apa yang harus dilakukan disana?"')
# print('Ibu berkata,"Belilah satu botol susu, jika ada telur, belilah 6 telur"')
# print("Maka budi berangkat")
# print("Budi mulai berbelanja")

# Percabangan : langkah melompat jika kondisi terpenuhi
bottle_of_milk = 100
has_egg=True

print(f"Jumlah botol susu {bottle_of_milk}")

if bottle_of_milk > 0:
    print ("Budi mengecek uangnya cukup atau tidak, ternya cukup")
    if has_egg:
        print("Budi membeli 1 botol susu dan 6 telur")
    else:
        print("Budi membeli satu botol susu")
else:
    print("Budi tidak membeli 1 botol susu")

    
