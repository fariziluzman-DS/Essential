import math


def calculate_years(principal, interest, tax, desired):
    
    year = 0
   
    while(principal < desired):
       
        totalpi = (principal*interest)
        aftertaxed = totalpi*tax
        principal = (principal+totalpi)-aftertaxed
        year += 1
        if(principal == desired):
            year = 0

    print('Harus menunggu {} tahun '.format(year))

calculate_years(1000, 0.05,0.18,1100)
calculate_years(1200, 0.17, 0.05, 2000)
calculate_years(1500,0.07,0.6,5000)

def expandedform(num):
    num = str(num)
    panjang = len(num)
    jumlahNol = panjang-1
    out=''
    x= 0 #untuk iterasi nomor index list
    for item in range(panjang):
        if(num[x] != '0'):
            out += num[x]
        for item1 in range(jumlahNol):
            if(num[x] != '0'):
                out += '0'
        jumlahNol -=1
        if(item == panjang-1):
            break
        if(num[x] != '0'):    
            out += ' + '
        x+=1
    print(out)

expandedform(179958)

def towermaker(floor, blocksize):
    pjg , lbr = blocksize
    out = ''
    forsps = floor
    for item in range(floor):
        for item1 in range(lbr):
            for space in range((forsps*2)-2): #10 8 6 4 2 0
                out+=' '
            for item2 in range(pjg):#2 2 2, 6 6 6, 10 10 10
                out+='*'
            out+='\n'
        pjg += 4
        forsps-=1
        #out+='\n'
    print(out)

towermaker(3,(2,3))