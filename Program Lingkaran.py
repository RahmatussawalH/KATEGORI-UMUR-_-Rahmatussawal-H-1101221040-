print("MENCARI LINGKARAN")
print("1. LUAS LINGKARAN")
print("1. KELILING LINGKARAN")
mulai = int(input())
if mulai <= 1:
    print("LUAS LINGKARAN")
    print("Masukan Jari-Jari Lingkaran")
    jari = int(input())
    print("RUMUS : (L = 22/7 x jari x jari)")
    luas = float(22) / 7 * jari * jari
    print("L = 22/7 x " + str(jari) + " x " + str(jari))
    print("L = " + str(luas) + " cm")
    print("Jadi, Luas Lingkaran Adalah " + str(luas) + " cm")
else:
    print("KELILING LINGKARAN")
    print("Masukan Jari-Jari Lingkaran")
    jari = int(input())
    print("RUMUS : (K = 2 x 22/7 x jari)")
    keliling = 2 * 22 / 7 * jari
    print("K = 2 x 22/7 x " + str(jari))
    print("K = " + str(keliling) + " cm")
    print("Jadi, Keliling Lingkaran Adalah " + str(keliling) + " cm")
print("SELESAI")
