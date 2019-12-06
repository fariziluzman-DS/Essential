# # #Variabel

# # harga = 20000

# # #pengkondisian
# # #operator comparison
# # #operator aritmatika
# # if ( 1>0):
# #     action

# # while(condition):
# #     action
# # for i in range ( 10,0,-1 )

def checkplatnomor(plat):
    import datetime
    x = datetime.datetime.now()
    tanggal = str(x.date())
    tanggal = tanggal[-2:]
    
    platnomor = plat.split(' ')[1]
    print (platnomor)
    if((int(platnomor) % 2 == 0) == (int(platnomor) % 2 == 0)):
        print('Lanjut')
    else:
        print('Skip')

checkplatnomor( 'D 6969 AH' )

# plat = 'D 6969 AH'
# plat = plat.split(' ')
# print(plat[1])

