#Getting an input: NOTE this works when getting text fromm the user 
# name= input("Enter your name: ")
# print("Hello " + name, "Welcome home for breakfast")

# This is use for getting  number from the user
# num= eval(input("Enter a number: "))
# print("Your number square: ", num*num)
# NOTE:The (eval) function converts the text entered by the user into a number.
# OR
# num= float(input("Enter a number: "))
# print("Your number square: ", num*num)

# temp=eval(input("Enter your temperature in celsius: "))
# print("In Fahrenheit, that is ",+9/5*temp+32)

# temp=eval(input("Enter the temperature in celsius: "))
# f_temp= 9/5*temp*32
# print("In Fahrenheit, that is",+ f_temp)
# if f_temp > 212:
#     print("That temperature is above the boiling point.")
# else:
#     f_temp < 32
#     print("That temperature is below the freezing point.")

# *******************
# *******************
# *******************
# *******************
# for i in range(4):
#     print("*"*19)
# print(f"""*******************
# *                 *
# *                 *
# *******************""")

# *
# **
# ***
# ****
# for i in range(4):#(4,0,-1):
#     print("*"*(i+1))

# a= 512
# b= 41.48
# c= 5
# d= 282
# f= a-d/b+c
# print(round(f))


# for i in range(12):
#     user= eval(input("Enter a number: "))
#     num= user/100
#     print("The percentage of your number is",num)
# print("My Gee your've run out of loop, kindly run it again if you want or i will Blast you off!!!!")

# user= eval(input("Please enter your number: "))
# num= user*user

# print("The square of", user,"is",num, sep="  " )

# for i in range(10):
#     num = eval(input("Enter a number: "))
#     print("The square of your number is", num*num)
# print("You have run out of space, please purchase for new one.")

# for i in range(45,100,3):
#     print(i+1, "---TitanRoot")

#Roll a dice hundred times:
# for i in range (100):
#     print("Roll the Dice",i+1)

# for i in range(10):
#     print("Hello")

'''The program below ask the user for a number 
and prints it's square, the ask for
another number and prints its square,etc.
It does this three times and then print that the loop is done'''

# for i in range(3): 
#     num= eval(input("Enter a number: "))
#     print("The square of the number is", num*num)
# print("The loop is now done.")
 

 
# print("A")
# print("B")
# for i in range(5):
#     print("C")
# for i in range(5):
#     print("D")
# print("E")

# for i in range(100,1000,50):
#     print(i)

# for i in range(100):
#     print(i)  

# for wacky_name in range(100):
#     print(wacky_name)

# for i in  range(100):
#     print(i+1,"---Wacky_name")


# for i in range(4):
#     print(i+1, "---Greg")

# for i in range(3):
#     print(i+1, "---Scott")


#Here is an exampple program that counts down from 5 and then prints a message.
# for i in range(5, 0, -1):
#     print(i, end=" ")
# print("Blast off !!!!!!!") #NOTE: The end="" just keeps everything on the same line.

# for i in range (100):
#     print(i+1,"GregFabian232")
# print("Yo man you have inserted your name hundred times")


# OR:
#NOTE: Here they will not be numbered according to it's counting; like from 1-100
# for i in range (100):
#     print("GregFabian232")
#     i=i+1

# print("Yo man you have inserted your name hundred times")

# NOTE: we use the end="" to join two lines of sentence to become one at the terminal 
# print("This is to inform all programers in FESTAC:",end=" ")
# print("You will be having a practical exams on 22^nd of July 207

# for i in range(20):
#     user = eval(input("Enter a number: "))
#     a= user*user 
#     print("The square of:",user,"=",a,sep=' ')
# print("start again out of prerogative")

# for i in range(8,90,3):
#     print(i)

# Write the following program in to be in this form: AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG
for i in range(10):
    print("A",end=' ')
for i in range(7):
    print("B",end=' ')
for i in range(4):
    print("CD",end=' ')
print("E",end=' ')
for i in range(6):
    print("F",end=' ')
print("G")

''' Write a program that ask a user for their name and how many times 
to print it. The program should print out the user's name the specifies 
number of times.'''

# for i in range(50):
#     user= input("please enter your name: ")
#     print(i+1,user,sep='-- ')
# print("You can still enter more in future, just wait for my update coming up on 2/4/2025")