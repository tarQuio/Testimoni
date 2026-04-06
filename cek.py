nama = input("Masukkan nama: ")
nilai = int(input("Masukkan nilai: "))

if nilai >=75 and nilai <=100:
    status = "LULUS"
    pesan = "Selamat, pertahankan potensimu"
elif nilai < 75  and nilai >= 0:
    status = "BELUM LULUS"
    pesan = "Coba lagi tahun depan"
else:
    status = "NILAI TIDAK VALID"
    pesan = "Coba lagi"

print("-" * 40)
print(f"Halo {nama}, status kamu: {status}")
print(pesan)
