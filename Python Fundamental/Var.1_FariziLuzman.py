a = input('Jam Berapa Masuk Parkiran ? : ')
masuk = int(a)
b = input('Pagi / Malam ? : ')
c = input('Jam Berapa Keluar Parkiran ? : ')
d = input('Pagi / Malam ? : ' )
keluar = int(c)

if (b == 'Pagi'):
    b = 'AM'
else :
    b = 'PM'

if  (d == 'Malam'):
     d = 'PM'
else :
    d = 'AM'

if ( b != d ):
    a1 = ( 12 - masuk )
    a2 = ( a1 + keluar )
elif( b == d ) :
    a2 = ( keluar - masuk )
    if (a2 < 0):
        a2 = a2 + 24
    if (a2 == 0):
        a2 = 24
jam = a2

if ( jam <= 3 ):
        biaya = jam * 3000
elif( 3 <= jam < 19):
        biaya = 9000 + ((jam-3)* 1000)
if ( jam > 19):
        biaya = 25000

print('Anda parkir selama = ' + str(jam) + ' jam, anda harus bayar : ' + str(biaya))