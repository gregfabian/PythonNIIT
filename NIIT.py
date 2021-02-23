'''convert celsius to fahrenheit'''
# celsius=float(input("Enter temperature in celsius: "))
'''calculate tempersture in fahrenheit'''
# fahrenheit= (celsius*1.8)+32
# print("%.2f celsius= %0.2f fahrenheit"%(celsius,fahrenheit))





# name = input("What is your name?: ") 
# print("Hello,",name,"you are welcome back!" )


# def my_function(fname):
#     print("Hello," + fname + " welcome home!")

# my_function(input("what is your name: "))

# def greet_user():
#     name = input("Enter your name: ")
#     print("Hello ",name)

# greet_user()

# def greet_user(name: str):
#     print("Hello", name)

# greet_user("Emil")


# def add_num(num1, num2):
#     sum = num1 + num2
#     return sum

# # result = add_num(1, 3)
# # print(result)

# def hello_worl():
#     print("Hello world")

# def add():
#     a = 1 + 1
#     print(a)

# ben = add()
# ben = hello_worl()
# print(ben)
# hello_worl()
# hello_worl()
# hello_worl()
# hello_worl()
# hello_worl()

# def add():
#     a = 1 + 1
#     return a


# ben = add()
# print(ben)

# '''User input supplies function parameter'''

# def happyBirthday(person):
#     print("Happy Birthday to you!")
#     print("Happy Birthday to you!")
#     print("Happy Birthday, dear " + person + ".")
#     print("Happy Birthday to you!")

# def main():
#     userName = input("Enter the Birthday person's name: ")
#     happyBirthday(userName)

# main()


datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
{"class":'V', "section":'A'}]
for item in datalist:
   print ("Type of ",item, " is ", type(item))
   




'''Display any number of sum problems with a function.
Handle keyboard input separately.
'''

def sumProblem(x, y):
    sum = x + y
    sentence = 'The sum of {} and {} is {}.'.format(x, y, sum)
    print(sentence)

def main():
    sumProblem(2, 3)
    sumProblem(1234567890123, 535790269358)
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    sumProblem(a, b)

main()



'''Display a sum problems with a function returning a string,
not printing directly.
'''

def sumProblemString(x, y):
    sum = x + y
    return 'The sum of {} and {} is {}.'.format(x, y, sum)

def main():
    print(sumProblemString(2, 3))
    print(sumProblemString(1234567890123, 535790269358))
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    print(sumProblemString(a, b))

main()



'''Illustrate a global constant being used inside functions.'''

PI = 3.14159265358979   # global constant -- only place the value of PI is set

def circleArea(radius):
    return PI*radius*radius    # use value of global constant PI

def circleCircumference(radius):
    return 2*PI*radius         # use value of global constant PI

def main():
    print('circle area with radius 5:', circleArea(5))
    print('circumference with radius 5:', circleCircumference(5))

main()




menu = raw_input ("Hello, please choose form following options (1,2,3) and press enter:\n"
    "Option 1\n"
    "Option 2\n"
    "Option 3\n")

if menu == str("1"):
    savinginfile = raw_input ("Please, state your name: ")
    option1()
elif menu == str("2"):
    print ("Option 2")
elif menu == str("3"):
    print ("Option 3")

def option1():
    test = open ("test.txt", "rw")
    test.write(savinginfile)
    print ("Option 1 used")
    test.close()



import time
import os
print("Welcome!")
name = input("Please enter your name: ")
print("Hello",name, "! I am going to guess your most favorite type of music.")
time.sleep(2)
print("Please, choose from one of the following: ")
listening_time = ["1 - One hour a day", "2 - About two hours per day", "3 - three to four hours per day", "4 - Most of the day"]
print(listening_time)
how_often = int(input("I find myself listening to music..."))

def add_file_1(new_1):
    f = open("music.txt", "a")
    f.write("1 Hour")

def add_file_2(new_2):
    f = open("music.txt", "a")
    f.write("2 Hours")

def add_file_3(new_3):
    f = open("music.txt", "a")
    f.write("3 - 4 Hours")

def add_file_4(new_4):
    f = open("music.txt", "a")
    f.write("Most of the day")

if how_often == str('1'):
    add_file_1(new_1)
elif how_often == str('2'):
    add_file_2(new_2)
elif how_often == str('3'):
    add_file_3(new_3)
else:
    add_file_4(new_4)





import time
import os
print("Welcome!")
name = input("Please enter your name: ")
print("Hello",name, "! I am going to guess your most favorite type of music.")
time.sleep(2)
print("Please, choose from one of the following: ")
listening_time = ["1 - One hour a day", "2 - About two hours per day", "3 - three to four hours per day", "4 - Most of the day"]
print(listening_time)
how_often = int(input("I find myself listening to music..."))

f =open("music.txt", "a") 
if how_often == 1:
    f.write("1 Hour")
elif how_often == 2:
    f.write("2 Hours")
elif how_often == 3:
    f.write("3 - 4 Hours")
else:
    f.write("Most of the day")








print("Please, choose from one of the following: ")

listening_times = {1:"One hour a day", 
                   2:"About two hours per day", 
                   3:"Three to four hours per day", 
                   4:"Most of the day"}

for k in listening_times:
    print "    %d - %s" % (k, listening_times[k])

how_often = int(input("I find myself listening to music..."))

with open("music.txt", 'a') as f:
    f.write(listening_times[how_often])










def add_file(new_1, usr_hours_choise):
    with open("music.txt", "a") as f:
        f.write(usr_hours_choise)

if how_often == 1:
    add_file(new_1, "1 hour.")
elif how_often == 2:
    add_file(new_2, "2 hour.")
elif how_often == 3:
    add_file(new_3, "3 - 4 hour.")
elif how_often == 1:
    add_file(new_4, "most of the day.")