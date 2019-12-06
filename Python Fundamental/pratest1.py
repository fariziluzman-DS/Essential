def square():

    n  = input('masukin angka : ')
    x = list(n)
    for i in range(len(x)):
        a = int(x[i])
        b = str(a * a)
        print(b,end='')

square()
x = ['stheno', 'Anew', 'Jason', 'Yous']

def friendfilter(a):

    for i in range(len(a)):
        if(len (a[i]) == 4):
            print(x[i] + ' ' ,end ='')
        elif(len (a[i]) != 4):
            b = a[i]
            b.replace(a[i], '')

friendfilter(x)

def domainname(whatever):
    list_domain = whatever.split('.')
    if (len(list_domain) == 3):
        print(list_domain[1])
    elif(len(list_domain) == 2):
          print(list_domain[0].split('//')[1])

domainname('https://www.cnet.com')
domainname('https://github.com')

def countWords(string):
    counting = string.split(' ')
    print (len(counting))

countWords('Hari ini kurang tidur lagi')

def smallEnough(jumlah,value):
    nilai = 0
    for i in range (len(jumlah)):
        nilai += jumlah[i]
    if ( nilai < value ):
        print('True')
    else:
        print('False')

smallEnough([689,108], 303)

def removeDuplicate(string):
    hasil1 = string.split(' ')
    hasil2 = set(list(hasil1))
    print(hasil2)

removeDuplicate('alpha beta gamma gamma zeta')

def stringy(number):
    hasil = ''
    for i in range(number):
        if ( i % 2 != 0):
            hasil += '0'
        else:
            hasil += '1'
    print(hasil, end = '')
stringy(5)
          
def wave(a):
    hasil = []
    for i in range (len(a)):
        a = list(a)
        a[i] = a[i].upper()
        hasil.append(''.join(a))
        a[i] = a[i].lower()
    print(hasil)

wave('waduk')
