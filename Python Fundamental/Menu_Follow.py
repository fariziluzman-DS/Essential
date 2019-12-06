back = 'Y'
while (back == 'Y'):
    check = False
    while ( check == False ):
        menu = input('1.Belanja 2.Belajar 3.Exit : ')
        if(menu.isalpha() == True or menu.isdecimal() == False):
            print('Input angka saja')
        else:
            menu = int(menu)
            if(menu > 0 and menu < 4 ):
                check = True
            else:
                print('Masukkan angka 1-3')
    if ( menu == 1):
        print('Selamat Belanja')
    elif( menu == 2):
        print('Selamat Belajar')
    elif( menu == 3):
        break

    menu = input('Mau ke awal ? Y/N')