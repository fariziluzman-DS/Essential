produk = ['jeruk','kiwi','apel']
hargaproduk = [4000,6000,5000]

def printListProduk (): 
    hasil = ''
    for i in range(len(produk)):
        hasil += str(i+1) + '. '  + produk[i] + ' Rp. ' + str(hargaproduk[i]) + '\n'
    return hasil

def addproduk(item,price) :
    produk.append(item)
    hargaproduk.append(int(price))

def deleteproduct(no) :
    num= int(no) - 1
    produk.pop(num)
    hargaproduk.pop(num)

def updateharga(no,price) :
    num= int(no) - 1
    hargaproduk[num] = price

keluar = False
while (keluar==False) :
    print('1. show produk')
    print('2. add produk')
    print('3. update harga produk')
    print('4. delete produk')
    print('')
    check = False
    while (check == False ) :
        pilih = input ('pilih (1,2,3,4):')
        if ((pilih =='1') or (pilih=='2') or (pilih == '3') or (pilih == '4')) :
            check = True
        else :
            print ('pilihan salah')
    
    if int(pilih) == 1 :
        print('')
        print(printListProduk())
        print('')
    
    
    elif int(pilih) == 2 :
        print('')
        tambahproduk = input ('produk apa yang mau di tambah? ') 
        tambahharga = input ('berapa harga nya? ')
        addproduk(tambahproduk,tambahharga)
        print('')
        print(printListProduk())
        print('')

    elif int(pilih) == 3 :
            print('')
            print(printListProduk())
            print('')
            num = input ('produk nomor berapa yang ingin di update harga nya? ') 
            newprice = input ('berapa harga yang baru? ')
            updateharga(num,newprice)
            print('')
            print('berikut list yang baru')
            print(printListProduk())
            print('')

    elif int(pilih) == 4 :
            print('')
            print(printListProduk())
            print('')
            num = input ('produk nomor berapa yang ingin di hapus dari list? ')
            deleteproduct(num)
            print('')
            print('berikut list yang baru')
            print(printListProduk())
            print('')

    print('apakah mau kembali ke menu utama? ')
    check = False
    while (check == False ) :
        menu = input('ya/tidak :  ')
        if (menu == 'ya' or menu == 'tidak') :
            check = True
        else :
            print ('inputnya salah')
    if menu == 'tidak' :
        keluar = True
