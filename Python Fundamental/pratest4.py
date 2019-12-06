import math

# # from collections import Counter

# alpha = list('abcdefghijklmnopqrstuvwxyz')

# def alphasum(a):
#     total = 0
#     a = list(a)
#     for i in range(len(a)):
#         if ( a[i] == alpha[i] ):
#             total += i + 1
#         else:
#             total += 0
#     print(total)
# alphasum('abc')

# def alphanext(a,n):
#     a = list(a)
#     for i in range(len(a)):
#         if (a[i] == alpha[i]):
#             alpha[i] = alpha[i + n]
#         else:
#             alpha[i] = alpha[i]
#     # for j in range (len(alpha) - (len(alpha)-len(a))):
#     #     new += alpha[j][j:len(a)]
#     #     print(new)
#     for j in range (len(alpha) - (len(alpha)-len(a))):
#         new = slice(len(a))
#     print(alpha[new])

# alphanext('abc',2)

# def numberOfPairs(a):

#     b = ['red','green','blue']
#     dict1 = { i : 0 for i in b }
#     for i in range (len(a)):
#             if ( a[i] == 'red'):
#                 dict1['red'] += 1
#             elif( a[i] == 'green'):
#                 dict1['green'] += 1
#             elif( a[i] == 'blue'):
#                 dict1['blue'] += 1
#     c = math.floor(sum(dict1.values())/2)
#     print(c)

# myGloves = ['red','red','green','blue','green','blue','red']
# numberOfPairs(myGloves)

# def sumOdd(a):
#     total = 0
#     for i in a:
#         if(i % 2 != 0):
#             total += i
#         else:
#             total += 0
#     print(total)
# list1=[1,2,3,4,5,6,7,8,9]
# sumOdd(list1)

# def generateNum(b):

#     a =['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Okt','Nov','Des']
#     a = [a.upper() for a in a ]
#     dict1 = { i : 0 for i in a }
#     b = [b.upper() for b in b ]
#     for i in range (len(b)-(len(b)-1)):
#         if ( b[2][3:6] == 'JAN'):
#             dict1['JAN'] += 1
#         elif( b[2][3:6]== 'FEB'):
#             dict1['FEB'] += 2
#         elif( b[2][3:6] == 'MAR'):
#             dict1['MAR'] += 3
#         elif( b[2][3:6] == 'APR'):
#             dict1['APR'] += 4
#         elif( b[2][3:6] == 'MAY'):
#             dict1['MAY'] += 5
#         elif( b[2][3:6] == 'JUN'):
#             dict1['JUN'] += 6
#         elif( b[2][3:6] == 'JUL'):
#             dict1['JUL'] += 7
#         elif( b[2][3:6] == 'AUG'):
#             dict1['AUG'] += 8
#         elif( b[2][3:6] == 'SEP'):
#             dict1['SEP'] += 9
#         elif( b[2][3:6] == 'OKT'):
#             dict1['OKT'] += 10
#         elif( b[2][3:6] == 'NOV'):
#             dict1['NOV'] += 11
#         elif( b[2][3:6] == 'DES'):
#             dict1['DES'] += 12    
#     c = math.floor(sum(dict1.values()))  
#     if(len(b[1]) % 2 != 0):
#         print(b[3][0] + b[0][0] + b[1][0] + b[1][2] + '-' + b[2][1] + str(c) + b[2][9:11])
#     else:
#         print(b[3][0] + b[0][0] + b[1][0] + b[1][1:3] + '-' + b[2][1] + str(c) + b[2][9:11])
# list1 = ['Braun','Noel','12-Apr-1970','M']
# generateNum(list1)

# def sumTwoSmallest(a):
#     a.sort()
#     print(a[0] + a[1])

# list1 = [19,5,42,2,7]
# sumTwoSmallest(list1)

# x = [1,2,3,4,1,2,1]
# x = Counter(x)
# key = x[1]
# print(key)
# if (Counter(x).values == 1):
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









        

    

