# Program Pengelolaan Laundry
# I.S.: pengguna memilih salah satu nomor menu
# F.S.: menampilkan hasil sesuai nomor menu yang dipilih
import os

# konstanta
MAKSPELANGGAN = 80


#subrutin menu pilihan
def Menu(Pilih):
    print('==============================')
    print('         MENU LAUNDRY         ')
    print('==============================')
    print('1. Pengisian Data Pelanggan')
    print('2. Tambah Data Pelanggan')
    print('3. Tampilkan Data Pelanggan')
    print('0. Keluar')
    print()
    Pilih = int(input('Pilihan Anda? '))
    
    return Pilih


#subrutin menu tampilan
def MenuTampilan(PilihTampilan):
    print('=================================================')
    print('                  MENU TAMPILAN                  ')
    print('=================================================')
    print('1. Tampilkan Semua Data Pelanggan')
    print('2. Cari Data Pelanggan Berdasarkan Kode Pelanggan')
    print('3. Cari Data Pelanggan Berdasarkan Nama Pelanggan')
    print('4. Urut Jumlah Secara Ascending')
    print('5. Urut Jumlah Secara Descending')
    print('0. Kembali ke Menu Utama')
    print()
    PilihTampilan = int(input('Pilihan Anda? '))
    
    return PilihTampilan


#subrutin menentukan harga bayar berdasarkan tipe
def HargaBayar(Tipe, Jumlah):
    if (Tipe == "BIASA"):
       return Jumlah * 6000
    elif (Tipe == "SETRIKA"):
      return Jumlah * 8000
        
        
# subrutin isi data pelanggan
def IsiPelanggan(N, Nama, Alamat, KodePelanggan, Jumlah, Harga, Tipe):
    N = int(input('Masukan jumlah pelanggan : '))
    if N > MAKSPELANGGAN:
        print('Jumlah Pelanggan Melebihi Batas Maksimal!..tekan enter untuk ulangi')
        print()
        os.system('pause')
        os.system('cls')
        N = int(input('Masukan jumlah pelanggan : '))

    for i in range(N):
        os.system('cls')
        ElemenNama = str(input('Nama Pelanggan Ke-{}   : '.format(i + 1)))
        Nama[i] = ElemenNama.upper()
        
        ElemenAlamat = str(input('Alamat Pelanggan Ke-{} : '.format(i + 1)))
        Alamat[i] = ElemenAlamat
        
        if i + 1 < 10:
            ElemenKode = f'LD-8070{i+1}'
        else:
            ElemenKode = f'LD-807{i+1}'
        
        KodePelanggan[i] = ElemenKode
        
        ElemenJumlah = int(input('Jumlah (Kg)  Ke-{}     : '.format(i + 1)))
        Jumlah[i] = ElemenJumlah
        
        ElemenTipe = str(input('Tipe (Setrika/Biasa)  Ke-{}     : '.format(i + 1)))
        Tipe[i] = ElemenTipe.upper()
        
        Harga[i] = HargaBayar(Tipe[i],Jumlah[i])
        
        DataPelangganKeFile(Nama[i], Alamat[i], KodePelanggan[i], Jumlah[i], Harga[i])
        
    return N
        
        
# subrutin memasukkan data ke dalam file txt
def DataPelangganKeFile(Nama, Alamat, KodePelanggan, Jumlah, Harga):
    f = open('DataRiwayatPelanggan.txt', 'a')
    f.write(f'Nama Pelanggan    : {Nama}' + '\n')
    f.write(f'Alamat Pelanggan  : {Alamat}' + '\n')
    f.write(f'Kode Pelanggan    : {KodePelanggan}' + '\n')
    f.write(f'Jumlah (Kg)       : {Jumlah}' + '\n')
    f.write(f'Harga             : {Harga:,.0f} '+ '\n')
    f.write('=================================================\n')
    f.close()
    

# subrutin tambah pelanggan
def TambahPelanggan(N, Nama, Alamat, KodePelanggan, Jumlah, Tipe):
    
    os.system('cls')
    
    for i in range(N, N + JumlahBaru):
        os.system('cls')
        ElemenNama = str(input(f'Nama Pelanggan Ke-{i+1}   : '))
        Nama[i] = ElemenNama.upper()
        
        ElemenAlamat = str(input(f'Alamat Pelanggan Ke-{i+1} : '))
        Alamat[i] = ElemenAlamat
        
        if i + 1 < 10:
            ElemenKode = f'LD-8070{i+1}'
        else:
            ElemenKode = f'LD-807{i+1}'
        
        KodePelanggan[i] = ElemenKode
        
        ElemenJumlah = int(input('Jumlah (Kg)  Ke-{}     : '.format(i + 1)))
        Jumlah[i] = ElemenJumlah
        
        ElemenTipe = str(input('Tipe (Setrika/Biasa)  Ke-{}     : '.format(i + 1)))
        Tipe[i] = ElemenTipe.upper()
        
        Harga[i] = HargaBayar(Tipe[i],Jumlah[i])
        
        DataPelangganKeFile(Nama[i], Alamat[i], KodePelanggan[i], Jumlah[i], Harga[i])


# subrutin total pelanggan
def TotalPelanggan(N, KodePelanggan):
    TotalPelanggan = 0
    for i in range(N):
        if KodePelanggan[i] != '/':
            TotalPelanggan = TotalPelanggan + 1
    
    return TotalPelanggan


# subrutin mengurutkan jumlah secara ascending dengan bubble short
def UrutJumlahAsc(N, Nama, Alamat, KodePelanggan, Jumlah, Harga):
    for i in range(N-1):
        j = N-1
        while (j >= i+1):
                if(Jumlah[j] < Jumlah[j-1]):
                    #Nama bertukar
                    Temp = Nama[j]
                    Nama[j] = Nama[j-1]
                    Nama[j-1] = Temp
                    
                    #Alamat bertukar
                    Temp = Alamat[j]
                    Alamat[j] = Alamat[j-1]
                    Alamat[j-1] = Temp
                    
                    #KodePelanggan bertukar
                    Temp = KodePelanggan[j]
                    KodePelanggan[j] = KodePelanggan[j-1]
                    KodePelanggan[j-1] = Temp
                    
                    #Jumlah bertukar
                    Temp2 = Jumlah[j]
                    Jumlah[j] = Jumlah[j-1]
                    Jumlah[j-1] = Temp2
                    
                    # Harga bertukar
                    Temp = Harga[j]
                    Harga[j] = Harga[j-1]
                    Harga[j-1] = Temp
                    
                j = j - 1


# subrutin mengurutkan jumlah secara descending dengan minimum sort
def UrutJumlahDsc(N, Nama, Alamat, KodePelanggan, Jumlah, Harga):
    for i in range(N-1):
        Min = i
        for j in range(1, N):
            if Jumlah[j] > Jumlah[Min]:
                Min = j
                
                #Nama bertukar
                Temp = Nama[i]
                Nama[i] = Nama[Min]
                Nama[Min] = Temp
                
                #Alamat bertukar
                Temp = Alamat[i]
                Alamat[i] = Alamat[Min]
                Alamat[Min] = Temp
                
                #KodePelanggan bertukar
                Temp = KodePelanggan[i]
                KodePelanggan[i] = KodePelanggan[Min]
                KodePelanggan[Min] = Temp
                
                #Jumlah bertukar
                Temp2 = Jumlah[i]
                Jumlah[i] = Jumlah[Min]
                Jumlah[Min] = Temp2
                
                # Harga bertukar
                Temp = Harga[i]
                Harga[i] = Harga[Min]
                Harga[Min] = Temp
                


# subrutin pencarian data pelanggan berdasarkan kode pelanggan dengan sentinel
def CariKodePelanggan(N, KodePelanggan, Nama, Alamat, Jumlah, Harga, CariKode):
    i = 0
    KodePelanggan[N] = KodePelanggan

    while KodePelanggan[i] != CariKode:
        i = i + 1
    if i < N:
        print(f'Data Ditemukan pada indeks ke-{i+1}')
        print()
        print(f'Kode Pelanggan    : {KodePelanggan[i]}')
        print(f'Nama Pelanggan    : {Nama[i]}')
        print(f'Jumlah (Kg)       : {Jumlah[i]}')
        print(f'Harga             : {Harga[i]}')
        print(f'Alamat Pelanggan  : {Alamat[i]}')
        return i
    else:
        print('Data Tidak Ditemukan')
        return -1



# subrutin pencarian data pelanggan berdasarkan nama pelanggan
def CariNamaPelanggan(N, Nama, Alamat, KodePelanggan, Jumlah, Harga, CariNama):
    print('Hasil Pencarian:')
    print()
    Ketemu = False
    for i in range(N):
        if CariNama in Nama[i]: 
            print(f'Kode Pelanggan    : {KodePelanggan[i]}')
            print(f'Nama Pelanggan    : {Nama[i]}')
            print(f'Jumlah (Kg)       : {Jumlah[i]}')
            print(f'Harga             : {Harga[i]}')
            print(f'Alamat Pelanggan  : {Alamat[i]}')
            print()
            Ketemu = True
    if not Ketemu:
        print('Data tidak ditemukan.')


# subrutin tampil pelanggan
def TampilPelanggan(N, Nama, Alamat, KodePelanggan, Jumlah, Harga):
    print('=========================================================================================================================')
    print('                                             DAFTAR DATA PELANGGAN                                                       ')
    print('=========================================================================================================================')
    print('-------------------------------------------------------------------------------------------------------------------------')
    print('| No |   Kode Pelanggan  | Nama Pelanggan       | Jumlah (Kg) |       Harga       |                Alamat               |')
    print('-------------------------------------------------------------------------------------------------------------------------')
    for i in range(N) :
        HargaBayar = "{:,.0f}".format(Harga[i])
        print(f'| {i+1:<2} |     {KodePelanggan[i]:<8}      | {Nama[i]:<20} |    {Jumlah[i]:<2} Kg    |  Rp. {HargaBayar:<12} | {Alamat[i]:<35} |')
    print('-------------------------------------------------------------------------------------------------------------------------')
    print()
    print(f'Total Pelanggan : {TotalPelanggan(N, KodePelanggan)}')
    

# Badan Program Utama
# Penciptaan data pelanggan
Nama = ['/'] * MAKSPELANGGAN
Alamat = ['/'] * MAKSPELANGGAN
KodePelanggan = ['/'] * MAKSPELANGGAN
Tipe = ['/'] * MAKSPELANGGAN
Jumlah = [0] * MAKSPELANGGAN
Harga = [0] * MAKSPELANGGAN

N = 0
Pilih = 0
Pilih = Menu(Pilih)
while Pilih != 0:
    match Pilih:
        case 1:
            os.system('cls')
            N = IsiPelanggan(N, Nama, Alamat, KodePelanggan, Jumlah, Harga, Tipe)
            print()
            os.system('pause')
        case 2:
            os.system('cls')
            JumlahBaru = int(input('Masukkan jumlah pelanggan baru: '))
            TambahPelanggan(N, Nama, Alamat, KodePelanggan, Jumlah, Tipe)
            N = N + JumlahBaru
            print()
            os.system('pause')
        case 3:
            os.system('cls')
            PilihTampilan = 0
            PilihTampilan = MenuTampilan(PilihTampilan)
            while PilihTampilan != 0:
                match PilihTampilan:
                    case 1:
                        os.system('cls')
                        if N > 0:
                            TampilPelanggan(N, Nama, Alamat, KodePelanggan, Jumlah, Harga)
                        else:
                            print('Data Masih Kosong...')
                        print()
                        os.system('pause')
                    case 2:
                        os.system('cls')
                        if N > 0:
                            CariKode = str(input('Masukkan Kode Pelanggan yang dicari: '))
                            CariKodePelanggan(N, KodePelanggan, Nama, Alamat, Jumlah, Harga, CariKode)
                        else:
                            print('Data Masih Kosong...')
                        print()
                        os.system('pause')
                    case 3:
                        os.system('cls')
                        if N > 0:
                            CariNama = str(input('Masukkan Nama Pelanggan yang dicari: ')).upper()
                            CariNamaPelanggan(N, Nama, Alamat, KodePelanggan, Jumlah, Harga, CariNama)
                        else:
                            print('Data Masih Kosong...')
                        print()
                        os.system('pause')
                    case 4:
                        os.system('cls')
                        if N > 0:
                            UrutJumlahAsc(N, Nama, Alamat, KodePelanggan, Jumlah, Harga)
                            TampilPelanggan(N, Nama, Alamat, KodePelanggan, Jumlah, Harga)
                        else:
                            print('Data Masih Kosong...')
                        print()
                        os.system('pause')
                    case 5:
                        os.system('cls')
                        if N > 0:
                            UrutJumlahDsc(N,Nama,Alamat,KodePelanggan, Jumlah, Harga)
                            TampilPelanggan(N,Nama,Alamat,KodePelanggan, Jumlah, Harga)
                        else:
                            print('Data Masih Kosong...')
                        print()
                        os.system('pause')
                    case _:
                        os.system('cls')
                        print('Nomor menu tidak ada!')
                        print()
                        os.system('pause')
                            
                os.system('cls')        
                PilihTampilan = MenuTampilan(PilihTampilan)

        case _:
            os.system('cls')
            print('Nomor menu tidak ada!')
            print()
            os.system('pause')
    
    os.system('cls')
    Pilih = Menu(Pilih)