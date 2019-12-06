def z():
    return[0,5,{'makan' : lambda : lambda x : print('Hello' + x)}]

z()[2]['makan']()['fikri']     # Hello Fikri

def x():
    return{'nama' : lambda : lambda : [0,1,lambda y, z : print(y + z)]}

x()['nama']()()[2](2,2)