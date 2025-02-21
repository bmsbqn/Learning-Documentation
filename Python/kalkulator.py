def tambah(a, b):
  return a + b

def kurang(a, b):
  return a - b

def kali(a, b):
  return a * b

def bagi(a, b):
  return a // b

print("\nKalkulator Terminal")
print("Tekan Enter untuk memulai!")
input()

angka1 = int(input("Masukan angka: "))
angka2 = int(input("Masukan Angka: "))

print("\nPilih Operasi: ")
print("1. Tambah (+)")
print("2. Kurang (-)")
print("3. Kali (x)")
print("4. Bagi (/)")
print("5. Keluar")

pilihan = (input("\nMasukan Pilihan (1/2/3/4) :"))

if pilihan == "1":
  hasil = tambah(angka1, angka2)
  print(f"Hasil: {angka1} + {angka2} = {hasil}")

elif pilihan == "2":  
  hasil = kurang(angka1, angka2)
  print(f"Hasil: {angka1} - {angka2} = {hasil}")

elif pilihan == "3":
  hasil = kali(angka1, angka2)
  print(f"Hasil: {angka1} x {angka2} = {hasil}")

elif pilihan == "4":
  if angka2 == 0:
    print("Error! Angka tidak bisa dibagi 0")
  else:
    hasil = bagi(angka1, angka2)
    print(f"Hasil: {angka1} / {angka2} = {hasil}")

elif pilihan == "5":
  print("Keluar!")
