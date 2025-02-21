def biaya_parkir(jam_parkir):
  return 5000 if jam_parkir <= 2 else 5000 + (jam_parkir - 2) * 3000

jam_pakai = float(input("Input jumlah jam parkir anda: "))
total = biaya_parkir(jam_pakai)

print(f"Total: Rp.{total:,.0f}")