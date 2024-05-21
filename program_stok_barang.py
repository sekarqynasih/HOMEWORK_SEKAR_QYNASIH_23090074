import modul

print('ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ')
print('Selamat datang di program Manajemen Stok Barang!')
print('ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ')
print('Pilihan : ')
print('1. Tambah Data Barang')
print('2. Edit Data')
print('3. Hapus Data Barang')
print('4. Cari Data')
print('5. Tampilkan Data Barang')
print('6. Tampilkan Jumlah Data')
print('7. Keluar')
print('ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ')

while True:
    pilihan = int(input('Masukan Pilihan : '))
    print('=================')
    if pilihan == 1 :
        modul.tambah_data_barang()
    elif pilihan == 2 :
        modul.edit_barang()
    elif pilihan == 3 :
        modul.hapus_data_barang()
    elif pilihan == 4 :
        modul.cari_data()
    elif pilihan == 5 :
        modul.tampilkan_data()
    elif pilihan == 6 :
        modul.tampilkan_jumlah_data()
    else:
        pilihan == 7
        print('Terimakasih :D ')
        break

