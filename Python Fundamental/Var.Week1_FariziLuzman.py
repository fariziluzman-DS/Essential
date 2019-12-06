def DupString(string):
    i = 0
    slash = list(string)
    for char in slash:
        a = 0
        while ( a < i + 1):
            print(char,end='')
            a += 1
        i += 1
DupString('fikri')
print()

def DupStringDua(string):
    i = 0
    slash = list(string)
    for char in slash:
        a = 0
        while ( a < i + 1):
                print(str.upper(char)+'-',end='')
                a += 1
        i += 1
DupStringDua('fikri')
print()

# def DupStringDua(string):
#     s = ''
#     dup = a
#     for i in range(len(dup)):
#         for j in range(i,len(dup)-(len(dup)-i-1)):
#             s = dup[:i+1]
#             print(s,end='')
#     print()
# DupString('fikri')

def pyramid(n):

    num = 1
    for i in range(n):
        for j in range(0,n-i-1):
            print(' ',end='')
        for k in range(0,2*i+1):
            print('*',end='')
            num += 1
        print() 

pyramid(3)
