def main():

   check = False
   while(check == False):
    a = input('1. Belanja ? 2. Belajar ? 3. Exit ?: ')
    if(a.isdigit()) == True:
        menu = int(a)
        if ( menu > 0 and menu < 4 ):
         check = True  
        elif( menu == 3):
           exit()   
    else:
        print("Hanya menerima angka saja ! (1-3) bukan huruf ! ")
    
   if(menu == 1):
    check = False
    while ( check == False):
       b = input ('Menu Belanja anda adalah: \n1. Ayam Rp 20000 \n2. Sapi Rp 40000 \n3. Salmon Rp 50000 \n   Klik angka 4 untuk melanjutkan: ')
       if(b.isdigit()) == True:
          qn = int(b)
          if ( qn == 4 ):
             check = False
             while ( check == False):
              ayam = (input('   Masukkan jumlah ayam yang ingin dibeli : '))
              sapi = (input('   Masukkan jumlah sapi yang ingin dibeli : '))
              salmon = (input('   Masukkan jumlah salmon yang ingin dibeli : '))
              #if ( sal != ''):
                #break
              if (ayam.isdigit() and sapi.isdigit() and salmon.isdigit()) == True:
               check = True
               Total=((20000*int(ayam))+(40000*int(sapi))+(50000*int(salmon)))  
               print('Total belanja anda adalah Rp ' + str(Total))
              else:
               print('   Hanya menerima angka saja ! bukan huruf ! ')

   #Total=((20000*int(ayam))+(40000*int(sapi))+(50000*int(salmon)))  
   #print('   Total belanja anda adalah Rp ' + str(Total))

   if(menu == 2):
    check = False
    while ( check == False):
       b = input ('Mau hitung apa ?  \n1.Luas Segitiga \n2.Luas Trapesium  \n Klik angka (1-2) untuk melanjutkan: ')
       if(b.isdigit()) == True:
          ql = int(b)
          if ( ql == 1 ):
             check = False
             while ( check == False):
              a1 = (input(' Masukkan Alas : '))
              t1 = (input(' Masukkan Tinggi : '))
              #if ( sal != ''):
                #break
              if (a1.isdigit() and t1.isdigit()) == True:
               check = True
               Total=((int(a1)*int(t1))//2)
               print ('Luas Segitiga = '+ str(Total))
              else:
               print('   Hanya menerima angka saja ! bukan huruf ! ')
          else:
                check = False
                while ( check == False):
                  a2 = (input(' Masukkan Sisi 1 : '))
                  a3 = (input(' Masukkan Sisi 2 : '))
                  t2 = (input(' Masukkan Tinggi : '))
            
                  if (a2.isdigit() and a3.isdigit()and t2.isdigit()) == True:
                        check = True
                        Total=(((int(a2)+int(a3))*int(t2))//2)
                        print ('Luas Trapesium = '+ str(Total))
                  else:
                        print(' Hanya menerima angka saja ! bukan huruf ! ')
   restart = input ('Ingin kembali ke menu awal ? : ').lower()
   if  restart == 'iya': 
     # check = True
       main()
   else:
      exit()
main()


            


       


    
         
    
