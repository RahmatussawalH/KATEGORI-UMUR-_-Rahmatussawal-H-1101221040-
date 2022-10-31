print("MENCARI PERSEGI")
print("1. LUAS PERSEGI")
print("2. KELILING PERSEGI")
mulai = int(input())
if mulai <= 1:
    print("LUAS PERSEGI")
    print("Masukan Panjang Sisi Persegi")
    sisi = int(input())
    print("RUMUS :(L = sisi x sisi)")
    print("L = " + str(sisi) + " X " + str(sisi))
    luas = sisi * sisi
    print("L = " + str(luas) + " cm")
    print("jadi, luasnya adalah " + str(luas) + " cm")
else:
    print("KELILING PERSEGI")
    print("Masukan Panjang Sisi Persegi")
    sisi = int(input())
    print("RUMUS :(K = sisi x 4)")
    print("K = " + str(sisi) + " X 4")
    keliling = sisi * 4
    print("K = " + str(keliling) + " cm")
    print("jadi, kelilingnya adalah " + str(keliling) + " cm")
print("SELESAI")
