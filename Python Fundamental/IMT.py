a = int(input('Masukkan Berat badan anda : '))
b = int(input('Masukkan Tinggi badan anda: '))/100

imt = a // (b * b)

if (imt < 18.5):
    hasil = ' , Kurang'
elif ( 18.5 <= imt <=24.9): # ( imt => 18.5 and imt <= 24.9)
    hasil = ' , Ideal'
elif (25.0<= imt <= 29.9):
     hasil = ' , Berlebih'
elif (30.0<= imt <=39.9):
     hasil = ' , Sangat berlebih ! '
elif (imt > 29.9):
     hasil = ' , Dasar Gembrot'
print('IMT = ' + str(imt) + hasil )
     
