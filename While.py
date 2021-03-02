
# temp = 0    # Without the temp = 0 at the starting point it will give name error
# while temp != -1000:
#     temp = eval(input("Enter a temperature, (-100 to quit): "))
#     print("In Fahrenheit that is", 9/5*temp+32)


# temp =0
# while temp != -1000:
#     temp = eval(input("Enter a temperature, (-100 to quit): "))
#     if temp != -1000:
#         print("In Fahrenheit that is", 9/5*temp+32)
#     else:
#         print("Bye!")

# from random import randint
# guess = 0
# hidden_num = randint(1,5)

# while guess != hidden_num:
#     guess = int(input("Guess a secret number: "))
# print("Congrates you finally got it!")

# for i in range(10):
#     print(i) # Note is the same with using while
# '''==========='''
# i = 0
# while i < 10:
#     print(i)
#     i = i+1
'''NOTE here below that we do not need an else statement here, 
The condition 
on the while loop guarantees that we 
will only get to the print statement 
once the user enters a valid temperature. Until that point,
the program will be stuck 
in the loop, continually asking the 
user for a new temperature.'''

# temp = eval(input("Enter a temperature in celsuis: "))
# while temp< -273.15:
#     temp = eval(input("Impossible. Enter a valid temperature: "))
# print("In Fahrenheit, that is", 9/5*temp+32)

# i = 0 # You can start from 1 or 2
# while i < 50:
#     print(i)
#     i = i + 2
# print("Bye!")

# i = 0 
# while i < 10:
#     num = eval(input("Enter a number (0 to quit): "))
#     if num > 10:
#         print("Follow the range 1 to 10.")
#     elif num < 1:
#         break
# print("Are you tired?")


# while True:
#     temp = eval(input("Enter a temperature: "))
#     if temp == -1000:
#         print("Bye!")
#         break
#     print(9/5*temp+32)

# num = eval(input("Enter a number: "))
# i = 2
# while i < num and num % i != 0:
#    i = i + 1
# if i == num:
#     print("Prime")
# else:
#     print("Not prime")

# i = 1
# while i <= 51:
#     print(i)
#     i = i + 


# weight = 0
# while weight <=200:
#     weight= int(input("Enter your weight: "))

#     if weight < 0:
#         print("Invalid entry try again")
#     else:
#         print("Your weight in pounds is {:.2f}".format(weight * 2.204623))

# while True:
#     weight= int(input("Enter your weight: "))
#     if weight < 0:
#         print("Invalid weight Bye!")
#         break
#     print("Your weight in pounds is {:.2f}".format(weight * 2.204623))

'''=============================='''
# x = 10
# y = 2
# while (x>y):
#     print(y)
#     y+=8


# color = "Blue"
# number = 5

# count = 0
# attempt = 3
# name = "Greg"
# while attempt >= 0:
#     guess_name = input("What is your name? ")
#     if guess_name == name:
#         print("You guessed  correctly")
#         break
#     else:
#         print(f"You have {attempt} attempts left")
#     attempt -= 1
    # guess_color = input("Guess a color: ")

    # guess_number = int(input("Guess a number: "))

# n =2
# while n <= 10:
#     if n % 2 == 0:
#         print(n)
#         n = n + 2


# while True:
#     num = int(input("Enter an even number only: "))
#     if num % 2 == 0:
#         print("Number",num,"is an even number")
#     else:
#         if num % 2 != 0:
#             print("Number",num,"is an odd number")
#         break

# x = 2
# while x < 12:
#     if x % 2 == 0:
#         print(x,"is even")
#     else:
#         x += 1
#         continue
#     x += 1


'''======================================================'''
'''FOR LOOP'''
'''++++++++++++++++++++++++++++++++++++++++++++++++++++++'''
# friends = ["Joseph", "Glenn", "Sally"]
# for friends in friends:
#     print("Happy New Year: ",friends)
# print("Done!")
'''========================================================='''

# total = 0
# for num in [3,10,3,5]:
#     total = total + num
#     print(total)
'''=========================================================='''


smallest = None
for intervar in [41,12,9,74,15,3]:
    if smallest is None or intervar < smallest:
        smallest = intervar
print("Smallest: ",smallest)
    
largest = None
for intervar in [3,41,12,9,74,15]:
    if largest is None or intervar > largest:
        largest = intervar
print("Largest: ",largest) 