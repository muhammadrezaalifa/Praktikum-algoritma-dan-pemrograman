total = 0
barang = []
harga = []

while True:

    print("===== Waroeng Reza Alifa ======\n")
    print("========== Jalan Melati 77 ============\n")

    print("""Daftar menu\n
    1. kopi \t 10000
    2. teh \t 15000
    3. susu \t 20000
    4. es jeruk \t 25000
    """ )


    Nama = input("Masukkan nama anda :")
    Alamat = input("Masukkan alamat anda :")
    Telepon = input("Masukkan telepon anda :")
    Tanggal = input("Masukkan tanggal pembelian :")
    kode = int(input("pilih menu : "))


    if kode == 1:
        barang.append('kopi')
        harga.append('10000')
        total += 10000
    elif kode == 2:
        barang.append('teh')
        harga.append('15000')
        total += 15000
    elif kode == 3:
        barang.append('susu')
        harga.append('20000')
        total += 20000
    elif kode == 4:
        barang.append('es jeruk')
        harga.append('25000')
        total += 25000
    else:
        print('kode tidak valid')

    lanjut = input('lanjut belanja (y/t) : ')
    if lanjut == 't' :
        print("")
        print('Nama :', Nama)
        print('Alamat :', Alamat)
        print('Telepon :', Telepon)
        print('Tanggal :', Tanggal)
        print('Barang yang dibeli : ', barang)
        print('Total yang harus dibayar : ', total, '\n')
        uang = int(input('Masukkan uang pembayaran : '))
        if uang > total:
            print('Kembaliannya : ', uang - total)
        elif uang == total:
            print('Uang pas')
        else:
            print('Uangnya kurang', uang - total)
        break 
    print('Harga barangnya : ', harga)
