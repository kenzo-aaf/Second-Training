Jumlah_buku = 10
Jumlah_buku_yang_dibaca_dan_dipahami = 0
Total_jumlah_baca = 0
print('Baca semua buku')
print(f'Jumlah buku yang sudah di baca dan dipahami {Jumlah_buku_yang_dibaca_dan_dipahami}')
print('Baca Buku')
while Total_jumlah_baca < Jumlah_buku * 2:
    Total_jumlah_baca = Total_jumlah_baca + 1
    if Jumlah_buku_yang_dibaca_dan_dipahami == 9 :
        print(f'Buku {Jumlah_buku_yang_dibaca_dan_dipahami + 1 } belum paham')
    else:
        Jumlah_buku_yang_dibaca_dan_dipahami = Jumlah_buku_yang_dibaca_dan_dipahami + 1
        print(f'Buku ke {Jumlah_buku_yang_dibaca_dan_dipahami} sudah dibaca')

print(f'Jumlah buku yang sudah di baca dan dipahami {Jumlah_buku_yang_dibaca_dan_dipahami}')
if Jumlah_buku_yang_dibaca_dan_dipahami == Jumlah_buku :
    print('Semua buku sudah dibaca dan dipahami')
else:
    print(f'Tidak semua buku bisa dipahami')


