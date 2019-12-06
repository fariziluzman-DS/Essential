# # LIST PYTHON

# # def Hello ():
# #     print('Hello World')

# x = 'Fikri '
# def Hello1 ():
  
#     return 'Hello World' + x

# print(Hello1())

# # produk1 = 'Jeruk'
# # produk2 = 'Jeruk'
# x = 'Anggur'
# produk = ['Jeruk' , 'Kiwi' , 'Leci' , x]

# # Kita Bisa Akses
# # print(produk[0])
# # print(produk[1])
# # print(produk[2])
# # print(produk[3])

# # Extracting List Python
# # for i in produk:
# #     print(i)

# # UBAH ISI LIST
# produk[1] = 'Mango'
# print(produk[:])


# # Nambahin Produk
# produk.append('Pepaya')
# print(produk[:])

# # Hapus Element Terakhir
# produk.pop()
# print(produk[:])

# # Nambahin Element ke Index Tertentu
# produk.insert(0, 'Kubis')
# print(produk)

# # Delete Element in python specificly
# produk.pop(0)
# print(produk)


produk = ['Jeruk' , 'Kiwi' , 'Apel']
hargaproduk = [1000,2000,3000]

def printListProduk (): 
    hasil = ''
    for i in range(len(produk)):
        hasil += str(i+1) + '. '  + produk[i] + ' Rp. ' + str(hargaproduk[i]) + '\n'
    return hasil

print(printListProduk())

# APLIKASI INTERAKTIF
# MENU 1 . Show Produk, 2. Add Product ,3. Update Harga , 4.Delete Product