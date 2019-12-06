def is_float(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

def check_ans(masukan):
    check = True
    while (check):
        while (is_int(masukan)== False):
            masukan = input('ans (angka): ')

        while (is_float(masukan)== False):
            masukan = input('ans (angka): ')

        masukan = int(masukan)

        if (masukan >= 1 and masukan <=6):
            check = False
            break
        masukan = input('ans (1/2/3/4/5/6): ')

def removeVocal(a):
    inp = a
    vocal=['a','e','i','o','u']
    for i in inp.lower():
        if i in vocal:
            inp = inp.replace(i,"")
    print(inp)

removeVocal('fikri')

def cek_huruf(nama='', huruf=''):
    hasil=False
    for item in nama:
        if(item==huruf):
            hasil=True
            # return True
            # break
    if(hasil==True):
        print("bahwa {hasil} bila {nama} yang mengandung huruf {huruf}".format(hasil=hasil, nama=nama, huruf=huruf))
        return True
    else:
        return False

cek_huruf('fikri', 'a')
print()

def ganjilGenap(number):
    sisa = number%2
    if(sisa==0):
        print("{number} adalah bilangan genap".format(number=number))
    else:
        print("{number} adalah bilangan ganjil".format(number=number))

ganjilGenap (3)
print()

def maxNumber(num1='', num2='', num3='', num4='', num5=''):
    tempat = -999999
    item = [num1,num2,num3,num4,num5]
    for each_num in item:
        if(tempat<each_num):
            tempat=each_num
    print(str(item) + " maksimumnya adalah "+str(tempat))
maxNumber(11,12,13,14,15)
print()

def stringFilter(nama):
    cek=False
    tempat_int = []
    sementara= ''
    for item in nama:
        if (is_int(item)==True):
            sementara += item
            cek=True
        else:
            if (cek==True):
                # print("oper")
                sementara += ','
                cek=False

    tempat_int = sementara.split(",")
    print("angka2 yang ada adalah = "+str(tempat_int))

    for setiap_item in range(0,len(tempat_int)):
        ha = tempat_int[setiap_item]
        ha= int(ha)
        print(str(ha) + " tipe datanya "+str(type(ha)))
    print(sementara)

stringFilter('teasytd123')
print()

def cek_plat(nama):
    cek=False
    tempat_int = []
    sementara= ''
    for item in nama:
        if (is_int(item)==True):
            sementara += item
            cek=True
        else:
            if (cek==True):
                # print("oper")
                sementara += ','
                cek=False

    tempat_int = sementara.split(",")

    for setiap_item in range(0,len(tempat_int)):
        ha = tempat_int[setiap_item]
        if(is_int(ha)==True):
            ha= int(ha)
            sisa = ha%2
            if(sisa == 0):
                print(nama+" adalah nomer genap")
            else:
                print(nama + " adalah nomer ganjil")
cek_plat('D 6969 AH')


