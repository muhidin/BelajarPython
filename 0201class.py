# Deskripsi: Contoh program sederhana untuk menampilkan teks ke layar
print("Pemrograman Berbasis Objek (PBO)")
print("Semester 2") # menampilkan teks Semester 2

"""  
ini adalah sebuah komentar
ini juga
ini juga deh
ini juga 
"""

nama = "Fandi Maulana"
hobi: str = "Berenang"
umur = 20
usia: int = 21
nilai_ujian: float = 90.5
laki = True

print("Nama Lengkap:", nama)
print("Nama Lengkap: %s" % nama)
print("Usia:", umur)
print("Laki-laki:", laki)
nama = "Farhanul Aulia Rizki"
print("Nama Lengkap: %s, Usia: %d, Laki-laki: %r, Nilai: %f" % (nama, umur, laki, nilai_ujian))

# Konstanta
from typing import Final
PI: Final = 22/7
print("Nilai PI:", PI)

# Tampilkan Penjumlahan, Pengurangan, Perkalian, Pembagian dan Modulus dari 2 variabel

nama_mahasiswa = ["Fandi", "Farhanul", "Aulia", "Rizki", "Maulana"]
print(nama_mahasiswa[3])

# Operator