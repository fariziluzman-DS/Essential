kumpulan = ['Merdeka', 'Hello', 'Hello', 'Sohib', 'kari Ayam']
keyword  = input('Mau Nyari Apa ? : ')
hasil = list(filter(lambda kata : keyword in kata,kumpulan))
print(hasil)

tahun = [1980,1999,1981,1990]

def genap (tahun):
    return tahun % 2 == 0

def dupfilter(fn,list1):
    newlist = []
    for item in list1:
        if fn(item) == True:
            newlist.append(item)
    return newlist
listgenap = dupfilter(genap,tahun)
print(listgenap)

