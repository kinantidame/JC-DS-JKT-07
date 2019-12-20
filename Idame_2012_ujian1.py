#IdameKinanti
#UjianFundamental

# Solve1: Input string, return # + capitalized words
# def hashtag(string):
#     new_s = string.split(' ')
#     new_s1 = []
#     for i in new_s:
#         new_s1.append(i.capitalize())
#     words = ''.join(new_s1)
#     if len(words) <= 140 and len(words)!=0:
#         print('#' + words)
#     else:
#         print('False')

# hashtag("Hello there how are you doing")
# hashtag("   Hello   World  ")
# hashtag("")

#Solve2 : Input Int, return Phone num
# def create_phone_number(number):
#     x = number
#     for i in x:
#         if len(x) == 10 and i <= 9:
#             return print(f"({x[0]}{x[1]}{x[2]}) {x[3]}{x[4]}{x[5]}-{x[6]}{x[7]}{x[8]}{x[9]}")
#         else:
#             print('Too much/less numbers. Please re-input.')
# create_phone_number([1,2,3,4,5,6,7,8,9,0])

#Solve 3: Sort Odd Even in same list
def sort_odd_even(num):
    if len(num)==False:
        return num
    else :
        even_bw = []
        odd_as = []
        for i in num:
            if i % 2 == 0 or i==0:
                even_bw.append(i)
            else:
                odd_as.append(i)
        odd_new = sorted(odd_as)
        even_new = sorted(even_bw, reverse=True)
        ###print(num) -c
        ###print(odd_new)-c
        ###print(even_new) -c
        for i,j in zip(num,odd_new):
            if i % 2==0 or i==0:
                pass
            else:
                if i > j:
                    i*=0
                    i+=j
                elif i < j:
                    pass
        for i,k in zip(num,even_new):
            if i % 2==0 or i==0:
                if i < k:
                    i*=0
                    i+=k
                elif i > k:
                    pass
            else:
                pass
    return print(num)
sort_odd_even([5,3,2,8,1,4])

# Solve4: Hollow Triangle
# def hollowTriangle(height):
#     z= ''
#     for i in range (0,height,1):
#         for j in range (0, height+2):
#             if j >= height-i and j <= height+i:
#                 z += '#'
#             else: 
#                 z += '_'    
#         z += '\n'
#     print (z) 
# hollowTriangle(4)
