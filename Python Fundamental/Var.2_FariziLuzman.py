a = input('Mau Menghitung apa ? (1).Hari atau (2).Detik ? : ')
if (a == '1'):
    hari = int(input ('Berapa Hari : ?'))
    tahun = hari//360
    excess = hari % 360
    bulan = excess // 30
    hariexcess = excess % 30

    print(str(hari) + ' hari sama dengan ' + (str(tahun)) + ' tahun, ' + (str(bulan)) + ' bulan, ' + (str(hariexcess)) + ' hari, ')

elif (a == '2'):
    detik = int(input('Berapa detik : ?'))
    tahun = detik // 31536000
    excess = detik % 31536000 
    bulan = detik // 2592000
    hariexcess = excess % 360
    jam = detik //3600
    jamexcess = detik % 3600
    menit = jamexcess//60
    detikexcess = jamexcess % 60

    print(str(detik) + ' detik sama dengan ' + (str(tahun)) + ' tahun, ' + (str(bulan)) + ' bulan, ' + (str(hariexcess)) + ' hari, '+ (str(jam)) + ' jam, ' + (str(menit)) + ' menit, ' + (str(detikexcess)) + ' detik, ')

else:
    print('404')



    








