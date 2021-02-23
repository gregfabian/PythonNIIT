'''List'''
'''============================================'''
'''Generating random values'''
# import random
# import math
# numlist = []
# for i in range(5):
#     numlist.append(random.randrange(1, 9))
# for i in numlist:
#     print(i)
'''=============================================='''
'''Bubble sort (algorithm)'''
# 1. An outer loop in size each time 
# 2. The goal is to have the leagest number at the end of the list when 
#     the outer loop completes 1 cycle 
# 3. the inner loop starts comparing indexes at the beginning of the loop
# 4. check if list[index] > list[index + 1]
# 5. If so swap the index values
# 6. When the inner loop completes the largest number is at the end of the list
# 7. Decrement the outer loop by 1
# import random
# import math
# numlist = []
# for i in range(5):
#     numlist.append(random.randrange(1, 10))

# i = len(numlist) - 1
# while i > 1:
#     j =0
#     while j < i:
#         print("\nIs {} > {}".format(numlist[j], numlist[j + 1]))
#         if numlist[j] > numlist[j + 1]:
#             '''to swap this two you have to temporaily store one of the value'''
# '''temporary store value'''
        #     print("switch")
        #     temp = numlist[j] 
        #     numlist[j] = numlist[j + 1]
        #     numlist[j + 1]  = temp
        # else:
        #     print("Don't Switch")
        # '''to continue running the code inside the loop to have to increment j'''
        # j += 1
    #     for k in numlist:
    #         print(k, end=", ")
    #     print()

    # print("END OF ROUND")
# '''then ouside of the loop you need to decremnt i'''

    # i -= 1
# '''after our bubble sort is done we the say'''
# for k in numlist:
    # '''separate each value with a comoma '''
#     print(k, end=", ")
# print()

'''======================'''
'''functions in list'''
# import random
# import math


# numlist = []
# for i in range(5):
#     numlist.append(random.randrange(1, 10))

# numlist.insert(5, 10)

# numlist.remove(10)
# numlist.pop(2)
# for k in numlist:
#     print(k, end=", ")
# print()
'''====================='''
'''List comprehension'''
'''one line way of generating an interesting data'''
# import math

# evenlist = [i * 2 for i in range(10)]

# for i in evenlist:
    # print(i)
'''======================='''
'''to get power of value'''
# import math

# numlist = [1,2,3,4,5]
# list_of_values = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)]for m in numlist]
# for i in list_of_values:
#      print(i)
# print()

'''ten by ten list of list'''
# multi_dimensional_list = [[0] * 10 for i in range(10)]

# multi_dimensional_list[0][1] = 10
# print(multi_dimensional_list[0][1])

'''muti dimensional list'''
# list_Table = [[0]* 10 for i in range(10)]
# for i in range(10):
#     for j in range(10):
#         list_Table[i][j] = "{} : {}".format(i, j)


# for i in range(10):
#     for j in range(10):
#         list_Table[i][j] = "{} : {}".format(i, j)
#         print(list_Table[i][j], end=" |!| " )
#     print()
'''=============================='''
'''creating a mutiplication table'''

#Creating the mutidimensional list
'''you say i want to create ten of them:'''
# mutiTable = [[0] * 10 for i in range(10)]
#Increment with outer for
# for i in range(1, 10):

    #Increment with inner for 
    # for j in range(1, 10):



        #Assign the value to the cell
        # mutiTable[i][j] = i * j


#Output the data
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(mutiTable[i][j], end=" , ")
#     print()