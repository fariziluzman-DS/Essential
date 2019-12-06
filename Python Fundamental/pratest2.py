def capitalize(a):
    hasil = []
    a = a.lower()
    genap = ''
    ganjil = ''
    for i in range (len(a)):
        if ( i % 2 == 0):
            genap += a[i].upper()
            ganjil += a[i]
        else:
            genap += a[i]
            ganjil += a[i].upper()
    hasil = [genap,ganjil]
    print(hasil)

capitalize('wadul')

def putar(a):
    a = a.split(' ')
    a.reverse()
    hasil = ''
    for i in range (len(a)):
        list1 = list(a)
        list2 = list(list1[i])
        list2.reverse()
        hasil += ''.join(list2)
        hasil += ' '
    print(hasil)
putar('budi sok nga wadul wae')

def sortstring(a,b):
    hasil = ''
    for i in range(len(b)):
        for j in range(len(a)):
            if ( b[i] == a[j]):
                hasil += a[j]
    for k in range (len(a)):
        if( a[k] not in hasil ):
            hasil += a[k]
    print(hasil)
sortstring('foos','of')

def likes(a):

    if(len(a) == 0):
        print('Nobody likes the show')
    elif(len(a) == 1):
        print(a[0] + ' likes the show')
    elif(len(a) == 2):
        print(a[0] + ' and ' + a[1] + ' likes the show' )
    elif(len(a) == 3):
        print(a[0] + ', ' + a[1] + ' and ' + a[2] + ' likes the show')
    elif(len(a) == 4):
        print(a[0] + ',' + a[1] + ' and 2 others likes the show')
    else:
        print('System Error')
list1 = ['Peter', 'North','Alex', 'John', 'Greg']
likes(list1)





