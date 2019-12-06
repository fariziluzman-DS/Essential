import math

def findeven(x,n):
  y = []
  for item in x:
      if ((item not in y) and (item % 2 == 0) ):
          y.append(item)
  print(y[1:n+1])
x = [1,2,3,4,5,6,7,8,9,10] 
findeven(x,3)

def findOdd2(x,n):
  y = []
  for item in range (len(x)):
        if((item not in y) and (item % 2 == 0)):
          y.append(x[item])
  print(y)
x = [1,2,3,4,5,6,7,8,9,10]
findOdd2(x,3)

def sortString(a,b):

  hasil = ''
  for i in range(len(b)):
    for j in range(len(a)):
      if(b[i] in a[j]):
        hasil += a[j]
      else:
        hasil = hasil 
  for k in range(len(a)):
    if(a[k] not in hasil ):
      hasil += a[k]
  print(hasil)

sortString('foos','of')

def hapusDup(a):

  hasil = []
  z = a.split(' ')
  for item in z:
    if ( item not in hasil):
      hasil.append(item)
  print(*hasil)
  print(*hasil, sep = ',')
hapusDup('alpha beta gamma gamma')

#Dictionary

dict1 = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
dict1.update( {'year' : 2019} )
dict1.update( {'color' : 'black'} )
del dict1['year']

for key in dict1:
  print(key)

for key in dict1:
  print(key, '->', dict1[key])

za_item = dict1.keys()
print(za_item)

for item in dict1.items():
  print(item)

for key, value in dict1.items():
  print(key, '->', value)

values = dict1.values()
print(values)

for value in dict1.values():
  print(value)

def uniq(a):

    num = {}
    for item in data:
        if (item in num.keys()):
            num[item] += 1
        else:
            num[item] = 1
    print(num)
    uniq = []
    for key,value in num.items(): # for i in namakamus cuman cetak key
        if(value == 1):
            uniq.append(key)
    print(uniq)
                
data = [1,1,3,6,3]
uniq(data)

def numberOfPairs(a):

    b = ['red','green','blue']
    dict1 = { i : 0 for i in b }
    for i in range (len(a)):
            if ( a[i] == 'red'):
                dict1['red'] += 1
            elif( a[i] == 'green'):
                dict1['green'] += 1
            elif( a[i] == 'blue'):
                dict1['blue'] += 1
    c = math.floor(sum(dict1.values())/2)
    print(c)

myGloves = ['red','red','green','blue','green','blue','red']
numberOfPairs(myGloves)

def sumOdd(a):
    total = 0
    for i in a:
        if(i % 2 != 0):
            total += i
        else:
            total += 0
    print(total)
list1=[1,2,3,4,5,6,7,8,9]
sumOdd(list1)

def generateNum(b):

    a =['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Okt','Nov','Des']
    a = [a.upper() for a in a ]
    dict1 = { i : 0 for i in a }
    b = [b.upper() for b in b ]
    for i in range (len(b)-(len(b)-1)):
        if ( b[2][3:6] == 'JAN'):
            dict1['JAN'] += 1
        elif( b[2][3:6]== 'FEB'):
            dict1['FEB'] += 2
        elif( b[2][3:6] == 'MAR'):
            dict1['MAR'] += 3
        elif( b[2][3:6] == 'APR'):
            dict1['APR'] += 4
        elif( b[2][3:6] == 'MAY'):
            dict1['MAY'] += 5
        elif( b[2][3:6] == 'JUN'):
            dict1['JUN'] += 6
        elif( b[2][3:6] == 'JUL'):
            dict1['JUL'] += 7
        elif( b[2][3:6] == 'AUG'):
            dict1['AUG'] += 8
        elif( b[2][3:6] == 'SEP'):
            dict1['SEP'] += 9
        elif( b[2][3:6] == 'OKT'):
            dict1['OKT'] += 10
        elif( b[2][3:6] == 'NOV'):
            dict1['NOV'] += 11
        elif( b[2][3:6] == 'DES'):
            dict1['DES'] += 12    
    c = math.floor(sum(dict1.values()))  
    if(len(b[1]) % 2 != 0):
        print(b[3][0] + b[0][0] + b[1][0] + b[1][2] + '-' + b[2][1] + str(c) + b[2][9:11])
    else:
        print(b[3][0] + b[0][0] + b[1][0] + b[1][1:3] + '-' + b[2][1] + str(c) + b[2][9:11])
list1 = ['Braun','Noel','12-Apr-1970','M']
generateNum(list1)

def wave(a):
    hasil = []
    for i in range (len(a)):
        a = list(a)
        a[i] = a[i].upper()
        hasil.append(''.join(a))
        a[i] = a[i].lower()
    print(hasil)

wave('wadul')

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

def rowSumOddNumber(baris):

  out = ''
  angka = 1
  total = 0
  for i in range(baris):
    out += ' '*(((baris-1)-i)*2)
    for j in range(i+1):
      out += str(angka)
      if(angka < 10):
        out += '   '
      else:
        out += '  '
      if( i == baris - 1 ):
        total += angka
      angka += 2
    out += '\n'
  print(out)
  print(total)

rowSumOddNumber(5)

