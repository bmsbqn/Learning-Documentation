def sisa_waktu(x):
  jam = x // 60
  menit = x % 60
  return jam, menit

x = int(input("Masukan Menit: "))
jam, menit = sisa_waktu(x)

print(f"Sisa waktu: {jam} Jam {menit} menit")