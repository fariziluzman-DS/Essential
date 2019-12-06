import math
def remove_outlier(a):

    listx2 = [71,70,73,70,70,69,70,72,71,300,71,69]
    listQ1 = []
    listQ3 = []
    listOut = []
    listx.sort()
    Q0 = 0
    Q1 = 0
    Q3 = 0

    for i in range(6):
        if(i != listx[i]):
            listQ1.append(listx[i])

    for j in range(6,12):
        if(j != listx[i]):
            listQ3.append(listx[j])

    # def getMedian(x):
    #     median = 0
    #     if(len(x) % 2 != 0):
    #         median += [math.floor(len(x)/2)]
    #     else:
    #         mid1 = x[(int(len(x)/2))-1]
    #         mid2 = x[(int(len(x)/2))]
    #         median += (mid1 + mid2) / 2

    if(len(listx) % 2 != 0):
        Q0 += [math.floor(len(listx)/2)]
    else:
        mid1 = listx[(int(len(listx)/2))-1]
        mid2 = listx[(int(len(listx)/2))]
        Q0 += (mid1 + mid2) / 2

    if(len(listQ1) % 2 != 0):
        Q1 += [math.floor(len(listQ1)/2)]
    else:
        mid1 = listQ1[(int(len(listQ1)/2))-1]
        mid2 = listQ1[(int(len(listQ1)/2))]
        Q1 += (mid1 + mid2) / 2

    if(len(listQ3) % 2 != 0):
        Q3 += [math.floor(len(listQ3)/2)]
    else:
        mid1 = listQ3[(int(len(listQ3)/2))-1]
        mid2 = listQ3[(int(len(listQ3)/2))]
        Q3 += (mid1 + mid2) / 2

    iqr = Q3 - Q1

    lowerLimit = Q1 - (1.5*iqr)
    upperLimit = Q3 + (1.5*iqr)

    y = math.ceil(lowerLimit)
    z = math.ceil(upperLimit)

    for k in listx2 :
        if( (k > y) and (k < z)):
            listOut.append(k)
    print( 'data asli = ' + str(listx2))
    print( 'data setelah di sort = ' + str(listx))
    print( 'setengah data pertama = ' + str(listQ1))
    print( 'setengah data terakhir = ' + str(listQ3))
    print( 'q1 adalah = ' + str(Q1))
    print( 'q3 adalah = ' + str(Q3))
    print( 'lower limit adalah  = ' + str(lowerLimit))
    print( 'upper limit adalah  = ' + str(upperLimit))
    print( 'data yang tidak outlier adalah = ' + str(listOut))
listx = [71,70,73,70,70,69,70,72,71,300,71,69]
remove_outlier(listx)

def countVocal(a):
    inp = 0
    vocal=['a','e','i','o','u']
    for i in a:
        if i in vocal:
            inp += 1
    print(inp)
countVocal('Budi pergi ke pasar')

def given(a):
    y = []
    for i in range(len(a)):
        for j in range(len(a) + i):
            if(i not in y):
                y.append(a[i][j])
    print(y)

given([[3,2,1],[4,6,5]])

def countWords(a):
    
    num = {}
    z = a.split(' ')
    for item in z:
        if (item in num.keys()):
            num[item] += 1
        else:
            num[item] = 1
    for key, value in num.items():
        print('Jumlah kata' + ' ' +str(key) +  ' ada sebanyak' + ' ' +str(value))  
kata = ('jangan jangan kamu adalah aku')
countWords(kata)













