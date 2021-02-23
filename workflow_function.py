# def add_numbers(num1, num2):
#     return num1 + num2

# print("5 + 4 =", add_numbers(5, 4))

'''Any variable defined inside a function is called Local variable'''
'''while a global variable is a variable that is created outside a function'''
'''for global'''
# gbl_name = "sally"
# def change_name():
#     global gbl_name
#     #to get permission to print sammy
#     gbl_name = "sammy"

# change_name()
# print(gbl_name)


'''this will return none'''
# def get_sum(num1, num2):
#     sum = num1 + num2

# print(get_sum(5, 4))

'''====================================='''
'''solving equation with function'''
#Solve for x 
#x + 4 = 9

#x will always be the first value received and you only 
#will deal with addition


#Receive the string and split into variables
# def solve_eq(equation):
    # x, add, num1, equal1, num2 = equation.split()

#Convert the string into int
    # num1, num2 = int(num1), int(num2)

#Convert the result into a string and join it to the string "X ="
    # return "x = "+ str(num2 - num1)


#print()
# print(solve_eq("x + 4 = 9"))

'''======================================='''
'''Returning multiple values'''

# def mult_divide(num1, num2):
#     return (num1 * num2), (num1 / num2)

# mult, divide = mult_divide(5, 4)

# print("5 * 4 =",mult)
# print("5 / 4 =", divide)
'''========================================='''
'''returning a list of prime'''
#A prime can only be divided by 1 and itself
#5 is a prime 1 and 5 = positive factor
#6 is not prime 1,2,3,6

#Input max prime
#Use a for loop and ckeck if modulus == 0 True

# def is_prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# def get_primes(max_number):
#     list_of_primes = []
#     for num1 in range(2, max_number):
#         if is_prime(num1):
#             list_of_primes.append(num1)
#     return list_of_primes

# max_num_to_check = int(input("Search for primes up to : "))

# list_of_primes = get_primes(max_num_to_check)
# for prime in list_of_primes:
#     print(prime)
'''========================================'''
'''Adding an unknown number of arguments using splart operator'''
'''*args'''
# def sumAll(*args):
#     sum = 0 
#     for i in args:
#         sum += i

#     return sum
# print("Sum : ", sumAll(1,2,3,4,5))


'''calculating Area using multiple different functions''' 
'''Maths function'''
# import math

# def get_area(shape):
#     shape = shape.lower()
#     if shape == "rectangle":
#         rectangle_area()
#     elif shape == "circle":
#         circle_area()
#     else:
#         print("Please enter rectangle or circle")

# def rectangle_area():
#     length = float(input("Enter the length: "))
#     width = float(input("Enter the width: "))

#     area = length * width
#     print("The area of the rectangle is: ",area)


# def circle_area():
#     radius = float(input("Enter the radius: "))

#     area = math.pi * (math.pow(radius, 2))

#     print("The area of a circle is {:.2f}".format(area))
# def main():
#     shape_type = input("Get area for what shape: ")

#     get_area(shape_type)

# main()