# def kali(x):
#     if x < 2:
#         return 1
#     else:
#         return (x*tiga())
# def tiga():
#     return 3

# print(kali(1))

#Dictionary

# nama = { 
#     'depan' : 'ucup',
#     'belakang' : 'ucok',
# }
# print(nama['depan'])

#Matrix2D
produk = [
    ['Jeruk', 2000],
    ['Apel', 3000],
    ['Nanas', 5000]
]
# for i in range(len(produk)):
#     hasil += str(i+1) + '. ' + produk[i][0] + ' Rp ' + str(produk[i][1]) + '\n'
# print(hasil)
cart = [
    [0,3],
    [2,5]
]

biaya = ''
for i in range (len(cart)):
    index = cart[i][0]
    biaya += str(i+1) + '. ' + produk[index][0] + ' Rp ' + str(produk[index][1]) + ' x '+ str(cart[i][1]) + ' = ' + str(produk[index][1]*cart[i][1]) + '\n'
print(biaya)
