# num= input("Enter number: ")
# remainder= int(num) % 3
# print(remainder)

# }OR
# num= input("Enter number: ")
# num= int(num)
# remainder=num % 3
# print(remainder)

# while True:
#     num= input("Enter Number: ")
#     try:
#         remainder= int(num)% 3
#         print(remainder)
#         break
#     except ValueError:
#         print("......Invalide Number.....")


# num1= int(input("Enter first numbre: "))
# num2= int(input("Enter second number: "))

# if num1 == num2:
#     print("They're equal")
# else:
#     print("The numbers are not equal")
# print("Independent print statement")

# num= 10

# guess_num = int(input("Guess the number: "))


# if guess_num == num:
#     print("You win")
# elif guess_num < num:
#     print("Number too low guess again")
# else:
#     print("Number too high.")


# age= int(input("Enter your age: "))

# if age >= 0 and age<=10:
#     print("Hall A")
#     gender = input("Enter gender: ")
#     if gender.lower() == ('m' or "male"):
#         print("Room A")
#     elif gender.lower() == ('f' or "female"):
#         print("Room B")
#     else:
#         print("OHH, No space!") 
# if age >= 11 and age<=15:
#     print("Hall B")
#     gender = input("Enter gender: ")
#     if gender.lower() == ('m' or "male"):
#         print("Room B")
#     elif gender.lower() == ('f' or "female"):
#         print("Room C")
#     else:
#         print("OHH, No space!") 
# if age >=16 and age<=19:
#     print("Hall C")
#     gender = input("Enter gender: ")
#     if gender.lower() == ('m' or "male"):
#         print("Room C")
#     elif gender.lower() == ('f' or "female"):
#         print("Room D")
#     else:
#         print("OHH, No space!") 
# if age == 20:
#     print("Hall D")
#     gender = input("Enter gender: ")
#     if gender.lower() == ('m' or "male"):
#         print("Room D")
#     elif gender.lower() == ('f' or "female"):
#         print("Room E")
#     else:
#         print("OHH, No space!") 

# while True:
#     age = int(input("Enter your age, (enter '0' to quit"))
# try:
#     if age == 0:
#         print("Thanks for using this program!")
#         break
#     else:
#         if age >= 1 and age<=10:
#             print("move to hall A")
#         elif age >=10 and age<=15:
#             print("move to hall B")
#         elif age >= 16 and age<=19:
#             print("move to hall C")
#         elif age == 20:
#             print("your all is D")
#         else:
#             print("you are not eligible for this section. enter 0 to quit or enter a valid age")

'''NOTE: if you have a complicated condition that containns both, (and, or) 
you may need parentheses around the I(or) condition. Think of (and) as being like multiplication 
and (or) as being like addition. Example'''  

# from random import randint

# num= randint(1,10)
# guess = eval(input("Enter your guess: "))

# if guess == num:
#     print("You got it!")
# else:
#     print("sorry, The number is ", num)


# grade= int(input("Enter your grade: "))
# if grade>=80 and grade <90:
#     print("Your grade is a B.")

# score= int(input("Enter your score: "))
# if score >1000 or time >20:
#     print("Game over.")

# if not (score > 1000 or time > 20):
#     print("Game continues."

# score= int(input("Entre your score: "))
# time= int(input("Enter your time: "))
# if (score< 1000 or time>20) and turns_remaining==0:
#     print("Game over.")

# grade = int(input("Enter you score: "))

# if grade>= 90:
#     print("A")
#     print("Excellent")

    
# if grade>=80 and grade<90:
#     print("B")
#     print("Very Good")

# if grade>70 and grade<80:
#     print("C")
#     print("Good")


# if grade>=60 and grade<70:
#     print("D")
#     print("satisfactory")
    
# if grade<60:
#     print("F")
#     print("Poor")

# }OR

# grade = eval(input("Enter your score: "))    

# if grade>=90:
#     print("A")
# elif grade>=80:
#     print("B")
# elif grade>=70:
#     print("C")
# elif grade>=60:
#     print("D")
# else:
#     print("F")

# count1 = 0
# count2 = 0
# for i in range(10):
#     num= eval(input("Enter a number: "))
#     if num>10:
#         count1 = count1 + 1
#     if num == 0:
#         count2 = count2 + 1
# print("There are",count1,"numbers greater than 10.")
# print("There are",count2, "zeroes.")
)


'''==========================='''
# def greet():
#     print("Hi there")
#     print("Welcome aboard")

# greet()


# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome aboard")

# greet("Mosh","Hamedani")


# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome aboard")
# #-1 perform a task function#
# greet("Mosh","Hamedani")
# greet("John","Smith")

# def greet(name):
#     print(f"Hi{name}")

# def get_greeting("Mosh"):
#     return f"Hi {name}"


# message = get_greeting("Mosh")
# file = open("content.txt","w")
# file.write(message)
'''======================='''
# def greet(name):
#     print(f"Hi {name}")
# #returns none 

# print(greet("Mosh"))
'''======================'''
# def increment(number, by):
#     return number + by 

# print(increment(2, by=1))
'''======================'''
# def increment(number, by=1):
#     return number + by 

# print(increment(2))
'''===================='''
# def increment(number, by=1):
#     return number + by 

# print(increment(2, 5))
'''======================'''
# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total

# print(multiply(2, 3, 4, 5))
'''=========================='''
# def save_user(**user):
#     print(user)
# #Dictionary
# save_user(id=1, name="John", age=22)
'''=========================='''
# def fizz_buzz(input):
#     if (input % 3 == 0 and input % 5 == 0):
#         return "FizzBuzz"
#     if input % 3 == 0:
#         return  "Fizz"
#     if input % 5 == 0:
#         return "Buzz"
#     return input

# print(fizz_buzz(7))


    




'''==========================='''
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


