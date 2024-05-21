data = [
    {"nama_barang" : "Handphone", "stok_barang" : 70},
    {"nama_barang" : "HeadPhone", "stok_barang" : 100}
]

def tambah_data_barang():
    nama = str(input('Masukan Nama Barang : '))
    stok = int(input('Masukan Stok Barang : '))
    data_new = {'nama_barang' : nama, 'stok_barang' : stok}
    data.append(data_new)
    print('--- DATA BERHASIL DITAMBAHKAN --- ')
    print('\n')

def edit_barang():
    edit = int(input('Edit data index ke : '))
    nama_baru = str(input('Masukan nama barang : '))
    stok_baru = int(input('Masukan stok barang : '))
    data_baru = [('nama_barang',nama_baru),('stok_barang',stok_baru)]
    data[edit].update(data_baru)
    print('--- DATA BERHASIL DITAMBAHKAN ---')
    print('\n')

def hapus_data_barang():
    hapus = int(input('Hapus data index ke : '))
    data.pop(hapus)
    print('--- DATA BERHASIL DITAMBAHKAN --- ')
    print('\n')

def cari_data():
    print(' Pencarian ')
    items = []
    cari = str(input('Cari nama barang : ')).lower()
    for i in data :
        if cari in i['nama_barang'] :
            items.append(i)
    if items :
        for item in items :
            print(f'{item['nama_barang']} : {item['stok_barang']}')
    else :
        print('Tidak ada data',cari)
    print('\n')

def tampilkan_data():
    print(' DATA BARANG ')
    for i in data:
        print(f"{i["nama_barang"]} : {i["stok_barang"]}")
    print('\n')

def tampilkan_jumlah_data():
    print(f'Jumlah Data Tersimpan :  {len(data)} data')
    print('\n')