
# for i in [2,4,6,8,10]:
#     print("i=",i)

# for i in range(10):
#     print("i=",i)
# for i in range(2,10): 
#     print("i=",i)
# }modulus to check if a number is odd or even
# i=2
# print((i % 2)==0)

#use for loop through the list from 1 to 21  
# for i in range(1,21):
#use modulus to check that the result is NOT EQUAL to 0
    # if ((i % 2)!=0):
#print the odds
        # print("i=",i)
#use for loop through the list from 1 to 21
# for i in range(1,21):
#use modulus to check thaat the result is EQUAL to 0
    # if((i % 2)==0):
#print the even
        # print("i=",i)
# }float
# your_float=input("Enter a float: ")

# your_float=float(your_float)

# print("Round to 2 decimals: {:.2f}".format(your_float))

#Have a user enter their investment amount and expected interest
#Each year their investment will increase by their investment + their investment *interest rate is
#print out the earnings after a 10 year period

#Ask for the money invested + the interest rate
# money =input("How much to invest: ")
# interest_rate=input("Interest Rate: ")

#Convert the value to a float
# money=float(money)

#Convert value to a float and round the percentage rate by 2 digits
# interest_rate=float(interest_rate)* .01

#Cycle through 10 years using a for loop and range from 0 to 9
# for i in range(10):
#     money=money + (money * interest_rate)
    
#Output the result
# print("Investment after 10 years: {:.2}".format(money))

#NOTE:float 
# i= .11111111111111111111
# j= .00000000000000001000

# print("Answer: {:.12}".format(i+j))

#while loop
# import random

# rand_num = random.randrange(1,51)

# i=1  #NOTE this shows the value you will be incrementing in the while loop which is going to be defined before the loop 

# while(i != rand_num):# define the condition that while"true" we will continue looping (continue looping if it comes back as true) 
    # i+=1 #increment your iterate
# print("The random value is: ",rand_num)

#CONTINUE and BREAK
# i=1

# while i<= 20:
#     if (i % 2) ==0:
#         i+=1
#         continue

#     if i ==15:
#         break
#     print("Odd: ", i)
#     i+=1
'''================================'''
'''
How tall is the tree:5

    #
   ###
  #####
 #######
#########
    #
'''
#Use 1 while loop 3 for loops
#4 spaces : 1 hash
#3 spaces : 3 hashes
#2 spaces : 5 hashes
#1 space  : 7 hashes
#0 space  : 9 hashes

#Need to do
# 1. Decrement spaces by 1 each time through the loop
# 2. Increment the hashes by 2 each time through the loop
# 3. Save spaces to be stump by calculating tree height - 1
# 4. Decrement from tree height until it equals 0
# 5. Print spaces and then hashes for each row
# 6. Print stump spces and then 1 hash

#Get the number of rows for the tree
# tree_height= input("How tall is the tree: ")
#Convert into an integer
# tree_height=int(tree_height)
#Get the starting spaces for the top of the tree
# spaces= tree_height - 1
#There is on hash to start that will be incremented
# hashes = 1
#Save stump spaces til later
# stump_spaces = tree_height - 1
#Make sure the right number of rows are printed
# while tree_height != 0:
#Printthe spaces 
    # for i in range(spaces):
#end=""
        # print(' ', end="")

#Print hashes
    # for i in range(spaces):
    #     print('#', end="")

#Newline after each row is printed
    # print()
#That spaces is decremented by 1 each time
    # spaces -= 1

#That hashes is incremented by 2 each time 
    # hashes += 2

#Decrement tree height each time to jump out of the loop
    # tree_height -= 1
#Print the spaces before the stump and then the hash
# for i in range(stump_spaces):
#     print(' ',end="")

# print("#")

'''Function'''
'''================================'''
# def add_numbers(num1, num2):
#     return num1 + num2


# print("5 + 4 =", add_numbers(5,4))


# def change_name(name):
#     name= "Mark"

# name = "Tom"

# change_name(name)   

# print(name)

'''=============================================='''

# def change_name(name):
#     return "Mark"

# name = "Tom"

# name = change_name(name)   

# print(name)



# gbl_name = "Sally"

# def change_name():
#     global gbl_name
#     gbl_name = "Sammy"

# change_name()   

# print(gbl_name)


'''========================================================='''
#solve for x
# x + 4 = 9

# x will always be the 1st value received and you only
# will deal with addition

# Receive the string and split the string into variables
# def solve_eq(equation):
#      x, add, num1, equal, num2 = equation.split()

#      num1, num2 = int(num1), int(num2)

    #  return "x = "+str(num2 - num1) # convert the strings into ints

    
#convert the result into a string and join it to the string "x= "

# print(solve_eq("x + 4 = 9"))


'''====================================='''
# def mult_divide(num1, num2):
#     return (num1 * num2), (num1/num2)


# mult, divide = mult_divide(5, 4)

# print("5 * 4 =",mult)
# print("5 / 4 =",divide)

'''===================================='''
# A prime can only be divided by 1 and itself
# 5 is a prime 1 and 5 = positive factor
# 6 is not prime 1,2,3,6

#Input max prime
# Use a loop and check if modulus == 0 True

# def is_prime(num):
#     for i in range(2, num):
#         if (num % i) == 0:
#             return False

#     return True  # we do have a prime number

# def getprimes(max_number):

#     list_of_primes = []

#     for num1 in range(2, max_number):
#         if is_prime(num1):
#             list_of_primes.append(num1)

#     return list_of_primes
# max_num_to_check = int(input("search for prime up to : "))

# list_of_primes = getprimes(max_num_to_check)

# for prime in list_of_primes:
#     print(prime)

'''========================================='''
# def sumAll(*args):
#     sum = 0

#     for i in args:
#         sum += i

#     return sum
# print("sum: ", sumAll(1,2,3,4,5))

'''==================================='''
# import math
# import os

# def get_area (shape):
#     shape = shape.lower()

#     if shape == "rectangle":
#         rectangle_area()
#     elif shape == "circle":
#         circle_area()
#     else:
#         print("please enter rectangle or circle")

# def rectangle_area():
#     length = float(input("Enter the length: "))
#     width = float(input("Enter the width: "))

#     area = length * width

#     print("The area of the rectangle is ",area)

# def circle_area():
#     radius = float(input("Enter the radius: "))

#     area = math.pi * (math.pow(radius, 2))

#     print("The area of the circle is {:.2f}".format(area))  #{:.2f} NOTE:this shows that you want to use two decimal places with the format 

# def main():
#     shape_type = input("Get area for what shape: ")

#     get_area(shape_type)

# main()



# import random
# import math

# random_list = ["string",1.234,28]
# one_to_ten = list(range(10))
# random_list = random_list + one_to_ten
# print(random_list[0])
# print("list lenght: ", len(random_list))
# first3 = random_list[0:3]

# for i in first3:
#     print("{} : {}".format(first3.index(i),i))
# print(first3[0] * 3)
# print("string" in first3)
# print("Index of string: ",first3.index("string"))
# print("How many strings: ",first3.count("string"))
# first3[0] = "New String"

# for i in first3:
#     print("{} : {}".format(first3.index(i),i))
# first3.append("Another")

# for i in first3:
#     print("{} : {}".format(first3.index(i),i))


