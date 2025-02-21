def diskon_belanja(total_diskon):
  if total_diskon >= 200000:
    hasil_diskon = total_belanja * 0.10
    print("Anda mendapatkan diskon 20%")
  elif total_diskon >= 100000:
    hasil_diskon = total_belanja * 0.10
    print("Anda mendapatkan diskon 10%")
  else:
    hasil_diskon = 0
  
  total_bayar = total_belanja - hasil_diskon
  return total_bayar

total_belanja = int(input("\nMasukan total belanja pembeli: Rp. "))
total_setelah_diskon = diskon_belanja(total_belanja)

print (f"\nTotal Belanja anda: Rp. {total_belanja}")
print (f"Total Belanja anda setelah diskon: Rp. {total_setelah_diskon:,.0f}\n")