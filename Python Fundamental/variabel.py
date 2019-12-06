# INI KOMENTAR

#nama = 'fikri'
#nama = 10
#print(nama)

#type data

#a = 'ucup'
#b = 69
#c = True

#print(type(a))
#print(type(b))
#print(type(c))

#Operator Aritmatika ( +  - *  /  % ) (str(),int() )
#angka1 = 20 
#angka2 = 10
#angka3 = '8'
#angka4 = '7'

#print(angka1 + angka2)
#print(int(angka3) + int(angka4))
#print(angka1 + int(angka3))
#print(angka1 * int(angka3))
#print(int(angka3) / int(angka4)) #kalau mau bulat div nya //
#print(angka1 % angka2)
#print(angka1 * angka2)

#control flow / pengkondisian && operator comparison ( == === > < => =< )
#beda if dan elif, if semua kondisi di periksa, elif satu kondisi saja yang perlu true

#a = 5
#if (a > 4):
#    print('Hulaihi')
#else :
#    print ('Watuloh')

#Input Process Output
#angka = input('Masukkan Angka : ') #input hasilnya selalu string
#print('Anda Menginput Angka ' + angka)

#nama = input('Masukan Nama : ')
#umur = input('Masukkan Tahun Lahir : ')
#job = input('Masukan Pekerjaan : ')

#Tahun = 2019 -int(umur)

#print (nama + ' berumur ' + str(Tahun) + ' tahun' + ' , pekerjaan dia adalah ' + job)

n = input('Masukan Angka 1 : ')
x = input('Masukkan Angka 2 : ')
y = input('Pilih Operator ( + - * / ):  ') 
Angka1 = int(n)
Angka2 = int(x)

if (y == '+'):
    print ( Angka1 + Angka2)
else :
    print ( Angka1 - Angka2)

