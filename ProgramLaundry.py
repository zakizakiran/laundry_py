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
    print('==============================')
    print('         MENU TAMPILAN        ')
    print('==============================')
    print('1. Tampilkan Semua Data Pelanggan')
    print('2. Cari Data Pelanggan Berdasarkan Kode Pelanggan')
    print('3. Urut Jumlah Secara Ascending')
    print('4. Urut Jumlah Secara Descending')
    print('0. Kembali ke Menu Utama')
    print()
    PilihTampilan = int(input('Pilihan Anda? '))
    
    return PilihTampilan

# subrutin isi data pelanggan
def IsiPelanggan(N, Nama, Alamat, KodePelanggan, Jumlah):
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
        Nama[i] = ElemenNama
        
        ElemenAlamat = str(input('Alamat Pelanggan Ke-{} : '.format(i + 1)))
        Alamat[i] = ElemenAlamat
        
        if i + 1 < 10:
            ElemenKode = f'LD-8070{i+1}'
        else:
            ElemenKode = f'LD-807{i+1}'
        
        KodePelanggan[i] = ElemenKode
        
        ElemenJumlah = int(input('Jumlah (Kg)  Ke-{}     : '.format(i + 1)))
        Jumlah[i] = ElemenJumlah
        
    return N
        
# subrutin tambah pelanggan
def TambahPelanggan(N, Nama, Alamat, KodePelanggan, Jumlah):
    
    os.system('cls')
    
    for i in range(N, N + JumlahBaru):
        os.system('cls')
        ElemenNama = str(input(f'Nama Pelanggan Ke-{i+1}   : '))
        Nama[i] = ElemenNama
        
        ElemenAlamat = str(input(f'Alamat Pelanggan Ke-{i+1} : '))
        Alamat[i] = ElemenAlamat
        
        if i + 1 < 10:
            ElemenKode = f'LD-8070{i+1}'
        else:
            ElemenKode = f'LD-807{i+1}'
        
        KodePelanggan[i] = ElemenKode
        
        ElemenJumlah = int(input('Jumlah (Kg)  Ke-{}     : '.format(i + 1)))
        Jumlah[i] = ElemenJumlah


# subrutin total pelanggan
def TotalPelanggan(N, KodePelanggan):
    TotalPelanggan = 0
    for i in range(N):
        if KodePelanggan[i] != '/':
            TotalPelanggan = TotalPelanggan + 1
    
    return TotalPelanggan

# subrutin mengurutkan jumlah secara ascending dengan bubble short
def UrutJumlahAsc(N, Nama, Alamat, KodePelanggan, Jumlah):
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
                    
                j = j - 1

# subrutin mengurutkan jumlah secara descending dengan minumum sort
def UrutJumlahDsc(N, Nama, Alamat, KodePelanggan, Jumlah):
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

# subrutin pencarian data pelanggan berdasarkan kode pelanggan
def CariPelanggan(N, KodePelanggan, Nama, Alamat, Jumlah, CariKode):
    Ketemu = False
    i = 0
    while (i < N) and not Ketemu:
        if KodePelanggan[i] == CariKode:
            Ketemu = True
        else:
            i = i + 1
    if Ketemu:
        print('Data Ditemukan pada indeks ke-', i+1)
        print('Nama Pelanggan    : ', Nama[i])
        print('Alamat Pelanggan  : ', Alamat[i])
        print('Kode Pelanggan    : ', KodePelanggan[i])
        print('Jumlah (Kg)       : ', Jumlah[i])
        
        return i
    else:
        print('Data Tidak Ditemukan')
        return -1

# subrutin tampil pelanggan
def TampilPelanggan(N, Nama, Alamat, KodePelanggan, Jumlah):
    print('=====================================================================================================')
    print('                                         DAFTAR PELANGGAN                                            ')
    print('=====================================================================================================')
    print('-----------------------------------------------------------------------------------------------------')
    print('| No |   Kode Pelanggan  |    Nama Pelanggan    | Jumlah (Kg) |                Alamat               |')
    print('-----------------------------------------------------------------------------------------------------')
    for i in range(N) :
        print(f'| {i+1:<2} |      {KodePelanggan[i]:<8}     | {Nama[i]:<20} |    {Jumlah[i]:<2} Kg    | {Alamat[i]:<35} |')
    print('-----------------------------------------------------------------------------------------------------')
    print()
    print(f'Total Pelanggan : {TotalPelanggan(N, KodePelanggan)}')
    

# Badan Program Utama
# Penciptaan data pelanggan
Nama = ['/'] * MAKSPELANGGAN
Alamat = ['/'] * MAKSPELANGGAN
KodePelanggan = ['/'] * MAKSPELANGGAN
Jumlah = [0] * MAKSPELANGGAN

N = 0
Pilih = 0
Pilih = Menu(Pilih)
while Pilih != 0:
    match Pilih:
        case 1:
            os.system('cls')
            N = IsiPelanggan(N,Nama,Alamat,KodePelanggan, Jumlah)
            print()
            os.system('pause')
        case 2:
            os.system('cls')
            JumlahBaru = int(input('Masukkan jumlah pelanggan baru: '))
            TambahPelanggan(N, Nama, Alamat, KodePelanggan, Jumlah)
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
                            TampilPelanggan(N,Nama,Alamat,KodePelanggan, Jumlah)
                        else:
                            print('Data Masih Kosong...')
                        print()
                        os.system('pause')
                    case 2:
                        os.system('cls')
                        if N > 0:
                            CariKode = str(input('Masukkan Kode Pelanggan yang dicari: '))
                            CariPelanggan(N,KodePelanggan, Nama, Alamat, Jumlah, CariKode)
                        else:
                            print('Data Masih Kosong...')
                        print()
                        os.system('pause')
                    case 3:
                        os.system('cls')
                        if N > 0:
                            UrutJumlahAsc(N,Nama,Alamat,KodePelanggan, Jumlah)
                            TampilPelanggan(N,Nama,Alamat,KodePelanggan, Jumlah)
                        else:
                            print('Data Masih Kosong...')
                        print()
                        os.system('pause')
                    case 4:
                        os.system('cls')
                        if N > 0:
                            UrutJumlahDsc(N,Nama,Alamat,KodePelanggan, Jumlah)
                            TampilPelanggan(N,Nama,Alamat,KodePelanggan, Jumlah)
                        else:
                            print('Data Masih Kosong...')
                        print()
                        os.system('pause')
                
                os.system('cls')        
                PilihTampilan = MenuTampilan(PilihTampilan)
            
    
    os.system('cls')
    Pilih = Menu(Pilih)