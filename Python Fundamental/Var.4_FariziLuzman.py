back = 'Y'
while (back == 'Y'):
    check = False
    while ( check == False ):
        menu = input('Mau Cetak apa ? 1.Persegi 2.Segitiga Siku Atas 3.Segitiga Siku Bawah 4.Segitiga Sama Kaki ? : ')
        if(menu.isalpha() == True or menu.isdecimal() == False):
            print('Input angka saja')
        else:
            menu = int(menu)
            if(menu > 0 and menu < 5 ):
                check = True
            else:
                print('Masukkan angka 1-4')

    if ( menu == 1):
        check = False
        while(check == False):
            m=(input('Masukkan Jumlah sisi ( 1-10 ) : '))
            if(m.isalpha() == True or m.isdecimal() == False):
                print('Input angka saja')
            else:
                n = int(m)
                if(n > 0 and n <= 10 ):
                    check = True
                    for i in range (n):
                        for j in range(n):
                            print('* ',end='')
                        print()
                else:
                    print('Masukkan angka 1-10')

    if ( menu == 2):
        check = False
        while(check == False):
            m=(input('Masukkan Jumlah sisi ( 1-10 ) : '))
            if(m.isalpha() == True or m.isdecimal() == False):
                print('Input angka saja')
            else:
                n = int(m)
                if(n > 0 and n <= 10 ):
                    check = True
                    for i in range(n):
                        for j in range(0,i+1):
                            print('* ',end='')
                        print()
                else:
                    print('Masukkan angka 1-10')
    
    if ( menu == 3):
        check = False
        while(check == False):
            m=(input('Masukkan Jumlah sisi ( 1-10 ) : '))
            if(m.isalpha() == True or m.isdecimal() == False):
                print('Input angka saja')
            else:
                n = int(m)
                if(n > 0 and n <= 10 ):
                    check = True
                    for i in range(n,0,-1):
                        for j in range(0,i):
                            print('* ',end='')
                        print()  
                else:
                    print('Masukkan angka 1-10')

    if ( menu == 4):
        check = False
        while(check == False):
            m=(input('Masukkan Jumlah sisi ( 1-10 ) : '))
            if(m.isalpha() == True or m.isdecimal() == False):
                print('Input angka saja')
            else:
                n = int(m)
                if(n > 0 and n <= 10 ):
                    check = True
                    for i in range(0,n):
                        for j in range(0,n-i-1):
                            print(end=' ')
                        for k in range(0,i+1):
                            print('* ',end='')
                        print()
                else:
                    print('Masukkan angka 1-10')
                    
    menu = input('Mau ke awal ? Y/N')


