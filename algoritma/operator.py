# ==========================================
# Nama File: operator.py
# Tugas: Menggunakan Input, Aritmatika, Perbandingan, dan Logika
# ==========================================

# 1. Menggunakan input()
nilai_ujian = int(input("Masukkan nilai ujian anda: "))
nilai_absen = 85
skor_prestasi = 10

# 2. Menggunakan minimal 2 operator aritmatika (+ dan -)
# Operator aritmatika 1: Penjumlahan (+)
total_nilai_sementara = nilai_ujian + skor_prestasi 

# Operator aritmatika 2: Pengurangan (-)
nilai_akhir = total_nilai_sementara - 2  # Dikurangi potongan administrasi/keterlambatan
print("Nilai Akhir Anda:", nilai_akhir)

# 3. Menggunakan minimal 2 operator perbandingan (>= dan >)
# Operator perbandingan 1: >=
apakah_nilai_tinggi = nilai_akhir >= 80

# Operator perbandingan 2: >
apakah_absen_bagus = nilai_absen > 75

# 4. Menggunakan operator logika (and dan or)
# Menggunakan operator logika 'and'
lulus_reguler = apakah_nilai_tinggi and apakah_absen_bagus
print("Apakah Lulus Reguler?", lulus_reguler)

# Menggunakan operator logika 'or'
# Mendapat beasiswa jika nilai akhir sangat tinggi (>= 95) ATAU memiliki nilai absen sempurna (== 100)
dapat_beasiswa = (nilai_akhir >= 95) or (nilai_absen == 100)
print("Apakah Mendapat Beasiswa?", dapat_beasiswa)
