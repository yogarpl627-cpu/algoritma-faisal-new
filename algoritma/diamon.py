tinggi = 6

# Bagian Atas Segitiga (Termasuk baris tengah)
for i in range(tinggi):
    spasi = " " * (tinggi - i - 1)
    bintang = "." * (2 * i + 1)
    print(spasi + bintang)

# Bagian Bawah Segitiga (Diperbaiki)
for i in range(tinggi - 2, -1, -1):
    spasi = " " * (tinggi - i - 1)
    bintang = "." * (2 * i + 1)
    print(spasi + bintang)