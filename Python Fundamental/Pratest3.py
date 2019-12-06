import math

def nb_year(p0,percent,aug,p):
    
    year = 0
    percent = format(percent / 100, '.2f')
    z = float(percent)
    while ( p0 < p): 
        x = ( z * p0 )
        y = ( p0 + x + aug )
        p0 = y
        year += 1
    print ('Waktu yang dibutuhkan untuk memenuhi target = ' + str(year) + ' tahun')
nb_year(1000,2,50,1200)

# def tickets(x):

#     z = 0
#     for i in range (len(x)-1):
#         z += x[len(x)-i-2] - x[len(x)-i-3]
#     z = z + 75
#     if ( z < x[len(x)-1] ):
#         print('False')
#     else:
#         print('True')
# list1= [25,25,50,100]
# tickets(list1)

def tickets(line):
    m25,m50,m100 = 0,0,0
    for item in line:
        if (item == 25):
            m25 += 1
        elif(item == 50):
            m25 -= 1
            m50 += 1
        elif(item == 100):
            m25 -= 1
            if (m50 > 0):
                m50 -= 1
            else:
                m25 -= 2
    if(m25 < 0 or m50 < 0):
        print('NO')
    else:
        print('YES')
tickets([25,25,50,100,100])

# def oddPyramid():
#     n = int(input('Mau buat berapa baris ? : '))
#     num = 1
#     for i in range(n):
#         for j in range(0,n-i-1):
#             print(' ',end='')
#         for k in range(0,i+1):
#             print(str(num) + ' ',end='')
#             num += 2
#         print()
# oddPyramid()

# def rowSumOddNumbers(n):
#     start = n*(n-1) + 1
#     tot = 0
#     for i in range(n):
#         tot += start
#         start += 2
#     print(tot)
# print()
# rowSumOddNumbers(5)

def rowSumOddNumbers(baris):
    out = ''
    angka = 1
    total = 0
    for i in range (baris):
        out += ' '*((((baris-1)-i)*2))
        for j in range(i + 1):
            out += str(angka)
            if(angka < 10):
                out += '   '
            el





