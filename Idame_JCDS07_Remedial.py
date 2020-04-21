#IdameKinanti
#RemedialPython

#Solve1: Output Length of The shortest word in given sentence
# def find_short(text):
#     word_l = text.split()
#     word_c = []
#     for word in word_l:
#         word_c.append(len(word))
#     word_c = sorted(word_c)
#     return print(word_c[0])

# find_short("Many people get up early in the morning")
# find_short("Every office would getting newest monitor")
# find_short("Create new file after this morning")

#Solve2: How many times until 1 digit last
# def persistence(n):
#     num = str(n)
#     times = 0

#     if int(num) >= 10:
#         while True:
#             result = 1
#             for i in num:
#                 result *= int(i)      
#             times +=1
#             if result < 10:
#                 break
#             else:
#                 num = str(result)
#     else:
#         times = 0
    
#     return print(times)

# persistence(999)
# persistence(5)
# persistence(39)

#Solve3: Multiplication Table
def multiplication_table(row,col):
    z = ''
    for i in range(1,(row+1)):
        num = 1
        for j in range(0,col):          
            x = str(i*num) + ' '
            z += x
            num +=1
        z += '\n'
    print(z)           

# multiplication_table(3,3)
# multiplication_table(5,3)
multiplication_table(3,5)

#Solve4: Alphabet Position
# def alphabet_position(text):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     d = {'a': 1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
#     'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20,
#     'u': 21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
    
#     text = text.lower()
#     word_ind = []

#     for char in text:
#         if char not in alphabet:
#             pass
#         else:
#             word_ind.append(str(d[char]))
#     return print(' '.join(word_ind))

# alphabet_position("The sunset sets at twelve o'clock.")
# alphabet_position("it's never too late to try")
# alphabet_position("Have you done your homework?")