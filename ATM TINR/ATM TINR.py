﻿m1 = 3
c1 = 0
print("ATM TINR")
print("MASUKAN KARTU ATM")
print("VALIDASI PIN" + chr(13) + "MASUKAN PIN")
vs = int(input())
print("1. LANJUTKAN TRANSAKSI" + chr(13) + "0. KELUAR")
t = int(input())
if t == 1:
    while c1 < m1:
        print("MASUKAN KODE PIN")
        sa = int(input())
        if sa == vs:
            c1 = 3
            print("PILIH TRANSAKSI" + chr(13) + "1. SETOR TUNAI" + chr(13) + "2. TARIK TUNAI" + chr(13) + "3. TRANSFER" + chr(13) + "4. CEK SALDO" + chr(13) + "0. KEMBALI")
            m2 = 10
            c2 = 0
            s = 0
            while c2 < m2:
                p = int(input())
                if p >= 1 and p <= 1:
                    print("SETOR TUNAI")
                    print("MASUKAN NOMINAL SETORAN")
                    st = int(input())
                    s = s + st
                    print("JUMLAH TABUNGAN ANDA Rp " + str(s) + ".000,00")
                else:
                    if p >= 2 and p <= 2:
                        print("TARIK TUNAI")
                        print("MASUKAN NOMINAL")
                        tr = int(input())
                        if tr < s:
                            tb = s - tr
                            print("JUMLAH TABUNGAN ANDA Rp " + str(tb) + ".000,00")
                            print("AMBIL UANG")
                        else:
                            print("SALDO ANDA TIDAK MENCUKUPI")
                    else:
                        if p >= 3 and p <= 3:
                            print("TRANSFER")
                            print("MASUKAN NOMINAL DITARIK")
                            tr = int(input())
                            if tr < s:
                                tb = s - tr
                                print("MASUKAN NO REKENING")
                                n = int(input())
                                print("TRANSFER SUKSES" + chr(13) + "Transfer Ke Rekening : " + str(n) + " Nominal Transfer : Rp " + str(tr) + ".000,00")
                                print("JUMLAH TABUNGAN ANDA Rp " + str(tb) + ".000,00")
                            else:
                                print("SALDO ANDA TIDAK MENCUKUPI")
                        else:
                            if p >= 4 and p <= 4:
                                print("CEK SALDO")
                                print("JUMLAH SALDO ANDA Rp " + str(s) + ".000,00")
                print("1. TRANSAKSI LAIN" + chr(13) + "0. KELUAR")
                p = int(input())
                if p == 0:
                    c2 = 10
                else:
                    c2 = c2 + 1
                    print("PILIH TRANSAKSI" + chr(13) + "1. SETOR TUNAI" + chr(13) + "2. TARIK TUNAI" + chr(13) + "3. TRANSFER" + chr(13) + "4. CEK SALDO" + chr(13) + "0. KEMBALI")
        else:
            print("COBA LAGI")
            c1 = c1 + 1
print("AMBIL KARTU ATM")
