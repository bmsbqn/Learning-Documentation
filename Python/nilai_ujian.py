def cek_nilai(tugas, uts, uas):
    return (tugas * 0.20) + (uts * 0.35) + (uas * 0.45)

print("\nCek Kelulusan\n")
tugas = float(input("Nilai Tugas: "))
uts = float(input("Nilai UTS: "))
uas = float(input("Nilai UAS: "))

hasil = cek_nilai(tugas, uts, uas)

print(f"Nilai Akhir: {hasil:.2f}")  
print("\nLulus" if hasil >= 60 else "Tidak Lulus") 