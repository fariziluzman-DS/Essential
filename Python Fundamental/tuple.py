# DICTIONARY

# nama = {
#     "depan" : "Fikri",
#     "belakang" : "jamaludin",
# }

# nama["tengah"] = 'Susilo'
# print(nama)
# Tuple

# Like list, but cannot be changed

# t = ('f' , [1 , True] , {"nama" : "fikri"})
# t[1].append('Tuple')
# t[2]['nama'] = 'purwadhika'

# Error 
# t[2] = {'akhir' : 'susilo'}
# print(t)

# Tuple Inside Tuple

# t = ( 1 ,'fikri' , ("purwadhika" , [True , False]))
# print(t.index('fikri'))


# Sets
# Doesnt support indexing
# Every item unique

# abc = {3,2,4,5,1,2}

# newList = [1,3,2,'test1' , 'test2' , 'test1',2,1 , '2','1']
# s = set(newList)
# print(s)



# LIST COMPREHENSION

# newList = ['fikri' , 'seto' , 'andi' , 'susilo' ]

# for a in newList:
#     print(a)

# list2 = []
# for item in newList:
#     list2.append(item + ' purwadhika')

# list2 = [item + ' purwadhika' for item in newList]

# tahun = [1990,1978,1980,1992]
# age = [2019 - item for item in tahun]

# bintang =[j for i in range(1,3) for j in range(2)]
# for i in range(1,3):
#     for j in range(2):
#         bintang.append(j)
        
# print(bintang)



# Lambda Expression

# def namaFunc():
#     print('hello')

# def x (num,num2):
#     return num * num2

# x = lambda num,num2 : num * num2


# print(x(4,5))



# MAP

# newList = [1,3,2,3,4,5]
# def kali(x):
#     return x * 2

# list2 = list(map(kali, newList))
# print(list2)

# tahun = [1990,1978,1980,1992]

# def umur(tahunlahir):
#     return 2019-tahunlahir

# listUmur = map(umur , tahun)
# print(list(listUmur))
# def dupMap(fn , listAja):
#     newList = []
#     for item in listAja :
#         newList.append(fn(item))
#     return newList

# listumur = dupMap(umur,tahun)
# print(listumur)


# Lambda with Map
# def umur(tahunlahir):
#     return 2019-tahunlahir
# tahun = [1990,1978,1980,1992]
# age = list(map(lambda tahunLahir : 2019 - tahunLahir , tahun ))
# print(age)

# Filter
# tahun = [1990,1945,1977,1978,1980,1992]

# newList = list(filter(lambda tahun : tahun % 2 ==0 , tahun ))
# print(newList)


# Method For Searching

# numlist = [2,3,4,1,10]
# check = 10 in numlist
# print(check)


# MATRIX list 2d
# produk = ['Jeruk' , 'Apel' , 'Anggur']
# harga = [2000 , 30000 , 40000]

# produk = [
#     ['jeruk' , 2000],
#     ['Apel' , 30000],
#     ['Anggur' , 40000]
# ]

# cart = [
#     [2,5],
#     [1,4],
#     [0,3]
# ]

# length = len(cart) 
# out =''
# for i in range(length):
#     index = cart[i][0]
#     out += str(i+1) + '. ' + produk[index][0] + ' Rp. ' 
#     + str(produk[index][1]) + ' x ' 
#     + str(cart[i][1]) + ' = ' 
#     + str(produk[index][1]*cart[i][1])  +'\n'

# print(out)
# produk[2][1]

# out = ''
# i = 0
# while(i < len(produk)):
#     out += str(i+1) + '. ' + produk[i][0] + ' Rp. ' + str(produk[i][1]) + '\n'
#     i +=1
# print(out)

# x = [3,3,6,8,9]

# def ulala(n):
#     return n > 3

# def dupfilter(fn,list):
#     temp = []
#     for item in list:
#         if(fn(item) == True):
#             temp.append(item)
#     return(temp)
# y = dupfilter(ulala,x)
# print(y)

# list COMPREHENSION
# bulan = [ 'Jan', 'Feb', 'Mar']
# searchValue = input('Mau Nyari Apa ? : ')
# newlist = [item for item in bulan if searchValue.lower() in item.lower()]
# print (newlist)

# lam = lambda x,y,z : x+y == z
# print(lam(2,2,4))

x = [1,2,3,2,5,7,2]
list.sort(x)
print(x)