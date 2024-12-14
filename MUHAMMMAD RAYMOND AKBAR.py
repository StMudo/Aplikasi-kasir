import datetime as dt

daftar_barang = {
    "magelangan": 12000,
    "indomie": 7000,
    "nutrisari": 5000,
    "teh": 3000,
    "nasi goreng": 15000,
}

pembelian = {}

def menu():
    print("1. magelangan = Rp. 12.000")
    print("2. indomie tante = Rp. 7.000")
    print("3. Nutrisari = Rp. 5.000")
    print("4. nasi goreng = Rp. 15.000")
    print("5. Teh = Rp 3.000")

def jumlah_menu():
    while True:
        barang = input("Masukkan nama barang (selesai untuk selesai): ").lower()
        if barang == "selesai":
            return
        if barang in daftar_barang:
            jumlah = int(input(f"Jumlah {barang}: "))
            if barang in pembelian:
                pembelian[barang] += jumlah
            else:
                pembelian[barang] = jumlah
        else:
            print("Barang tidak tersedia. Silakan coba lagi.")

def totalbelanja():
    total_tagihan = 0
    for barang, jumlah in pembelian.items():
        total_tagihan += daftar_barang[barang] * jumlah
    return total_tagihan

def kembalian(jumlhuang):
    return jumlhuang - totalbelanja()

def struk(nama, tagihan, uang, kembalian):
    waktu = dt.datetime.today()
    print("=============")
    print("====STRUK====")
    print("=============")
    print(f"NAMA : {nama}")
    print("Tagihan : ", tagihan)
    for barang, jumlah in pembelian.items():
        print(f"{barang}: {jumlah} pcs")
    print("Uang : ", uang)
    print("Kembalian : ", kembalian)
    print("Waktu pemesanan : ", waktu)

while True:
    namapelanggan = input("MASUKAN NAMA PELANGGAN : ")
    menu()
    jumlah_menu()
    print("=================================")
    print("Barang yang di beli : ")
    for barang, jumlah in pembelian.items():
        print(f"{barang}: {jumlah} pcs")
    print("===================================")
    print("total : ",totalbelanja())
    jumlhuang = int(input("MASUKAN JUMLAH UANG : "))
    print(pembelian)
    struk(namapelanggan, totalbelanja(), jumlhuang, kembalian(jumlhuang))
