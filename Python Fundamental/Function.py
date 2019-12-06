# Functon

# def NamaFunc():

# def Halo():
#     print('Well Shit, What A Great New Fucking Day !')

# Halo()

# def blender(buah):
#     print('jus ' + buah)

# blender(buah = 'Kemem')

# def HitungParkir(masuk=0,keluar=0): #parameter petama bisa gak ditentuin default value nya
#         TotalJam = abs(keluar - masuk)
#         TotalBiaya = TotalJam * 3000
#         print(TotalBiaya)

# HitungParkir(7,12)

# def removeChar(a,b):
#     # old = a
#     # remove = b
#     # new = old.replace(remove,'')
#     print(a.replace(b, ''))

# removeChar('Purwadhika','i')

def BatuKertasGunting(player1,player2):

    if (player1 == 'kertas' and player2 == 'kertas'):
            print('DRAW')
    elif(player1 == 'batu' and player2 == 'batu'):
            print('DRAW')
    elif(player1 == 'gunting' and player2 == 'gunting'):
            print('DRAW')
    elif(player1 == 'kertas' and player2 == 'batu'):
            print( 'Player 1 WIN ! ')
    elif(player1 == 'gunting' and player2 == 'kertas'):
            print(' Player 1 WIN ! ')
    elif(player1 == 'batu' and player2 == 'gunting'):
            print(' Player 1 WIN ! ')
    elif(player2 == 'kertas' and player1 == 'batu'):
            print( 'Player 2 WIN ! ')
    elif(player2 == 'gunting' and player1 == 'kertas'):
            print(' Player 2 WIN ! ')
    elif(player2 == 'batu' and player1 == 'gunting'):
            print(' Player 2 WIN ! ')

BatuKertasGunting('kertas','batu')