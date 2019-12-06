#Persegi
n=int(input('Mau Berapa Sisi : ? '))
for i in range (n):
    for j in range(n):
        print('* ',end='')
    print()

Siku atas
n=int(input('Mau Berapa Sisi : ? '))
for i in range(n):
    for j in range(0,i+1):
        print('* ',end='')
    print()

Siku Bawah
n=int(input('Mau Berapa Sisi : ? '))
for i in range(n,0,-1):
    for j in range(0,i):
        print('* ',end='')
    print()

Segitiga
n=int(input('Mau Berapa Sisi : ? '))
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=' ')
    for k in range(0,i+1):
        print('* ',end='')
    print()







