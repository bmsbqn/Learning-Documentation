def cek_tahun_kabisat(tahun):
    return tahun % 400 == 0 or (tahun % 4 == 0 and tahun % 100 != 0)

print("Cek Tahun Kabisat")
cek = int(input("Masukkan Tahun: "))
hasil = cek_tahun_kabisat(cek)

if hasil:
    print("Tahun Kabisat!")
else:
    print("Bukan Tahun Kabisat!")
