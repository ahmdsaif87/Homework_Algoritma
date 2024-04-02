nama = input('Masukkan Nama : ')
umur = int(input('Masukkan umur : '))
kelamin = ('Laki-laki', 'Perempuan')
jenisKelamin = input('Jenis Kelamin : ')
wargaNegara = 'Indonesia'
wni = input('Warga negara mana : ')
kartuKeluarga = input('Apakah anda bawa Foto Copy KK (True/false) ? ').lower() == 'true'

if kartuKeluarga == True and umur >= 17 and jenisKelamin in kelamin and wni == wargaNegara :
    print('-' * 30)
    print(f'Nama : {nama}')
    print(f'Umur : {umur}')
    print(f'Jenis Kelamin : {jenisKelamin}')
    print(f'Kebangsaan : {wni}')
    print(f'Foto Copy KK : {kartuKeluarga}')
    print('Silahkan masuk ruangan untuk Foto dan Scan Sidik jari anda')
    print('-' * 30)
else :
    print('-' * 30)
    print(f'Nama : {nama}')
    print(f'Umur : {umur}')
    print(f'Jenis Kelamin : {jenisKelamin}')
    print(f'Kebangsaan : {wni}')
    print(f'Foto Copy KK : {kartuKeluarga}')
    print('Anda belum bisa membuat KTP hari ini')
    print('-' * 30) 