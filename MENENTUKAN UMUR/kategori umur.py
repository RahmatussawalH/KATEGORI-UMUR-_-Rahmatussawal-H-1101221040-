print("KATEGORI UMUR")
print("Silahkan Masukan Tahun Lahir Anda")
lahir = int(input())
usia = 2022 - lahir
print("Usia Anda " + str(usia) + " Tahun")
print("Anda Termasuk Golongan")
if usia <= 11:
    print("Anak-Anak")
else:
    if usia >= 12 and usia <= 25:
        print("Remaja")
    else:
        if usia >= 26 and usia <= 45:
            print("Dewasa")
        else:
            print("Lansia")
