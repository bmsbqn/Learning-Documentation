def jarak_tempuh(km, bensin):
  konsumsi_bensin = km // bensin
  return konsumsi_bensin


bensin = int(input("Kilometer bensin perliter: "))
jarak = int(input("Jarak tempuh (Kilometer): "))
hasil = jarak_tempuh(jarak, bensin)

print(f"\nJumlah liter yang dibutuhkan: {hasil} liter")