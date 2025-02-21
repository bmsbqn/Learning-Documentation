def cek_kelayakan_kredit(gaji, hutang):
  return gaji >= 5000000 and hutang <= 10000000
  
gaji_debitur = int(input("\nJumlah Gaji bulanan anda: Rp. "))
hutang_debitur = int(input("Jumlah hutang anda: Rp. "))
keputusan = cek_kelayakan_kredit(gaji_debitur, hutang_debitur)

if keputusan:
  print("\nSelamat! Anda telah memenuhi syarat kredit")
else:
  print("\nMaaf! Anda belum memenuhi syarat kredit")