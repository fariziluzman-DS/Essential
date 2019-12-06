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

def removeVocal(nama='', huruf=''):
    hasil  = nama.replace(huruf, "")
    print("# Awal: {nama} \n# do: menghapus huruf '{huruf}'\n# result: {hasil}".format(nama=nama,huruf=huruf,hasil=hasil))

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

def ganjilGenap(number):
    sisa = number%2
    if(sisa==0):
        print("{number} adalah bilangan genap".format(number=number))
    else:
        print("{number} adalah bilangan ganjil".format(number=number))

def maxNumber(num1='', num2='', num3='', num4='', num5=''):
    tempat = -999999
    item = [num1,num2,num3,num4,num5]
    for each_num in item:
        if(tempat<each_num):
            tempat=each_num
    print(str(item) + " maksimumnya adalah "+str(tempat))

def Filter_Integer(nama):
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
    # print(sementara)

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

print("======removal Vocal=======")
removeVocal('muhammad agfian', 'a')
print("\n")
print("======CEK HURUF=======")
a =  cek_huruf('muhammad agfian', 'd')
print(a)
print("\n")
print("======CEK Ganjil Genap=======")
ganjilGenap(9)
print("\n")
print("======CARI MAX=======")
maxNumber(1,4,100,3,9)
print("\n")
print("======Filter Inteeger=======")

Filter_Integer('no 1 Muhammad Agfian tingginya 165 cm, beratnya 50, dan umurnya 20')
print("\n")
print("======CEK Plat=======")

cek_plat("D 5468 GA")
print("\n")