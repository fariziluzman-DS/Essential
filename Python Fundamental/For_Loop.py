# for item in range (3,10,2):
#     print ('urutan ' + str(item))
#print(list(range(0,10)))

#Nested Loop
# out = ''                                  
# for i in range(3):                         
#     for i in range(4):                     
#         out += '*  '                       
#     out+= '\n'                             
# print(out)

# i = 0
# out = ''
# while ( i < 3):
#     j = 0
#     while( j < 4):
#         out += '*'
#         j += 1
#     out += '\n'
#     i += 1
# print(out)

# out = ''                                  
# for i in range(3):                         
#     for i in range(4):                     
#         out += '*  '                       
#     out+= '\n'                             
# print(out)

# out = ''
# for i in range (4):
#     for i in range (4):
#         out += str(i + 1)
#     out += '\n'
# print(out)

# out = ''
# for i in range (5,0,-1):
#     for j in range (0,i):
#         out += '*'
#     out += '\n'
# print(out)

# out = ''
# for i in range (0,5):
#     for j in range (1+i):
#         out += '*'
#     out += '\n'
# print(out)

out = ''
for i in range (10):
    for j in range (0,10-i-1):
        out += ' '
    for k in range(0,i+1):
        out += '* '
    out += '\n'
print(out)