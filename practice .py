
# print("Hello, World!")

# }free flow
# name=("what is your name ")
# print("Hello", name)

# }python indentation
# if 5>2:
#     print("Five is geater than two!")#spaces at the beginning of a code
# if 5>2:
#        print("five is greater than two!")#this is also good

# }creating variable:
# x=5
# y="Hello, World!"
# print(x)
# print(y)

# x="python is "
# y="awesome"
# z=x+y
# print(z)

# x=5
# y="John"
# print(x)
# print(y)

# x="awesome"
# print("python is " + x)

# x="python is "
# y="awesome"
# z=x+y
# print(z)

# }casting: 
#if you want to specify the data type of a variable,this can be done with casting
# x=4 # x is of type int
# x="greg" # x is of type str
# print(x)

# x=str(3) #x will be "3"
# y=int(3) #y will be 3
# z=float(3) #z will be 3.0
# print(x)
# print(y)
# print(z)

# x=5
# y="Chioma"
# print(type(x))
# print(type(y))

# }Single or double quotes:
# x="John"
# x='John'
# print(x)
# print(x)

# }Case-Sensitive:
# a=4
# A="Dock"
# print(a)
# print(A) #A will not overwrite a

# }Variable Names:
# myvar="John"
# my_var="Chioma"
# _my_var="Greg"
# myVar="Elochukwu"
# MYVAR="Ayo"
# myvar2="Josh"

# print(myvar)
# print(my_var)
# print(_my_var)
# print(myVar)
# print(MYVAR)
# print(myvar2)

# }multiple words variable names:
# $Camel case: myVariableName="John" #Easch word except the first, start with a capitsal letter 
# $Pascal case: MyVariableName="John" #Each word start with a capital letter
# $Snake case: my_variable_name="John" #Each word is separated by an underscore charater

# }Multiple Variables:
# x,y,z="Orange", "Banana","Cherry"
# print(x)
# print(y)
# print(z) # make sure the number of variables matches the number of values, or else you get an error

# }One value to multiple variables:
# x=y=z="Orange"
# print(x) #assigning same value to the variables
# print(y)
# print(z)

# }Unpacking:
# fruits=["Orange","Banana","Cherry"]
# x,y,z=fruits
# print(x)
# print(y)
# print(z)

# }output variables 
# x="python is "
# y="awesome"
# z=x+y
# print(z)

# x=5
# y=10
# print(x+y) #for numbers, the + character works as a mathematical operator
# x=5 
# y="John" 
# print(x+y) #it doesn't work this way

# }global variables/outside function
# x="awesome"

# def myfunc():
#     print("python is "+ x)      #varariable is created outside of a function and used inside the function

# myfunc()

# }global variable/inside function
# x="awesome"

# def myfunc():
#     x="fantastic"
#     print("python is "+ x)

# myfuc()

# print("python is "+ x)

# }global keyword
# x="awesome"

# def myfunc():
#     global x
#     x="fantastic"

# myfunc() #to change the value of a global variable inside a function, refer to the variable by using the global keyword

# print("python is "+ x) 

# }global scope 
# def myfunc():
#     global x # making the x belong to the global scope
#     x="fantastic" 

# myfunc()

# print("python is "+ x)

# }data types:  # you get the data type by using the type() function
# x=8
# print(type(x))

# }setting the data type 
# x="Hello World"
# print(x)  #str
# print(type(x))

# x=20
# print(x) #int
# print(type(x))

# x=20.5
# print(x) #float
# print(type(x))

# x=1j
# print(x) 
# print(type(x)) #complex

# x=["apple","orange","banana"]
# print(x)
# print(type(x)) #list

# x=("apple","banana","cherry")
# print(x)
# print(type(x)) #tuple

# x=range(6)
# print(x)
# print(type(x)) #range

# x={"name":"John","age":36}
# print(x)
# print(type(x))  #dict

# x={"apple","banana","cherry"}
# print(x)
# print(type(x))  #set

# x=frozenset({"apple","banana","cherry"})
# print(x)
# print(type(x)) #frozenset

# x=True
# print(x)  #bool
# print(type(x))

# x=b"Hello"
# print(x)
# print(type(x))  #bytes

# x=bytearray(5)
# print(x)
# print(type(x))  #bytearray

# x=memoryview(bytes(5))
# print(x)
# print(type(x))  #memoryview(bytes())

# }setting the specific data type 
# x=str("Hello World")
# print(x)
# print(type(x))

# x=int(20)
# print(x)
# print(type(x))

# x=float(20.5)
# print(x)
# print(type(x))

# x=complex(1j)
# print(x)
# print(type(x))

# x=list(("apple","orange","cherry"))
# print(x)
# print(type(x))

# x=tuple(("apple","banana","cherry"))
# print(x)
# print(type(x))

# x=range(8)
# print(x)
# print(type(x))

# x=dict(name="John",age=36)
# print(x)
# print(type(x))

# x=set(("apple","banana","cherry"))
# print(x)
# print(type(x))

# x=frozenset(("apple","banana","cherry"))
# print(x)
# print(type(x))

# x=bool(5)
# print(x)
# print(type(x))

# x=bytes(5)
# print(x)
# print(type(x))

# x=bytearray(5)
# print(x)
# print(type(x))

# x=memoryview(bytes(5))
# print(x)
# print(type(x))

# }numbers#variables of numeric types are created when you assign a value to them
# x=1 #int
# x=2.8 #float
# x=1j #complex

# }int 
# x=1
# y=35656222554887711
# z=-3255522
# print(type(x))
# print(type(y))
# print(type(z))

# }float
# x=1.10
# y=1.0
# z=-35.59
# print(type(x))
# print(type(y))
# print(type(z))

# }float can also be scientific numbers with an "e"to indicate the power of 10. 
# x=35e3
# y=12E4
# z=-87.7e100
# print(type(x))
# print(type(y))
# print(type(z))

# }complex 
# x=3+5j
# y=5j
# z=-5j
# print(type(x))
# print(type(y))
# print(type(z))

# }type conversion #you can convert from one type to another with int(),float(),& complex() methods:
# x=1
# y=2.8
# z=1j
# #convert from int to float: #convert to float
# a=float(x)
# #convert from float to int: #convert to int
# b=int(y)
# #convert from int to complex: #convert to complex
# c=complex(x)
# print(a)
# print(b)
# print(c)
# #checking the data type after conversion:
# print(type(a))
# print(type(b))
# print(type(c))
# NOTE: you cannot convert complex numbers into another number type. 

# }random number:
# NOTE: python does not have random()function to make a random number but has a built-in module called RANDOM

# import random
# print(random.randrange(1,10))

# }specifing data type 
#int()
# x=int(1)   #x will be 1
# y=int(2.8) #y will be 2
# z=int("3") #z will be 3
# print(x)
# print(y)
# print(z)

# #float()
# x=float(1)     #x will be 1.0
# y=float(2.8)   #y will be 2.8
# z=float("3")   #z will be 3.0
# w=float("4.2") #w will be 4.2
# print(x)
# print(y)
# print(z)
# print(w)

#str()
# x=str("s1")  #x will be 's1'
# y=str(2)     #y will be '2'
# z=str(3.0)   #z will be '3.0'
# print(x)
# print(y)
# print(z)

# # }strings #you can display string literal with the print() function
#NOTE:strings in python are arrays of bytes representing unicode characters.
# print("Hello") #double quotation mark
# print('Hello') #single quotation mark

# }assigning a string to a variable
# a="Hello"
# print(a) 

#multiline strings
# a= """Algorithm is a step by step process to solving a problem by analyzing the ideas.
# Flowchart is a graphical representation of an algorithm.
# Pseudocode is used to represent the logic of solving a problem"""
# print(a)
# NOTE:you can as well use a single quotation mark (''')
# NOTE:in the result, the line breaks are inserted at the same position as in the code

# }strings are arrays
#python does not have a charater data type,a single charater is simply a string with a length of 1.
#square brackets can be used to access elements of the string.
# a="Hello, World!"
# print(a[1])
#get the charater at position 1 (remember that the first charater has the position(0).)

# }Looping through a string
#NOTE:since strings are arrays,we can loop through the charaters in a string,with a (for)loop. 
# for x in "banana":
#     print(x)

# }string length #the len() function returns the length of a string 
#to get a length of a string,use the len()function
# a="Hello, World!"
# print(len(a))

# }checking string
#we can use the (in)keyword to check if a certain phrase or charater is present in a string.
# txt="The best thing in life are free!"
# print("free"in txt)

#use it in an (if)statement
# txt="The best things in life are free!"
# if "free"in txt:
#     print("yes, 'free' is present.")

# }check if NOT
#to check if a certain phrase or charater is not in a string, we can use the keyword (not in)
# txt="The best things in life are free!"
# print("expensive"not in txt)

#use it in an (if) statement
# txt="The best things in life are free!"
# if "expensive"not in txt:
#     print("yes, 'expensive' is NoT present.")

# }python slicing strings
#specify the start index, and the end index, separated by a colon, to return a part of the string

#slicing strings:
#get the characters from position 2 to 5(not included)
# b="Hello, World!"
# print(b[2:5])

# #slice from the start:
# b="Hello, World"
# print(b[:5])  #get the characters from the start to position 5 (not included)

#slice from the end:
# b="Hello, World!"
# print(b[2:])  #get the characters from position 2, and all the way to the end

# }Nagative indexing:
# NOTE:use negative index to start the slicing from the end of the string:
# b="Hello, World!" #From: "o"in "World!"(position -5)
# print(b[-5:-2])  # To, but not included: "d" in "World!" (position -2)

# }modify strings:
#upper case
# a= "Hello, World!"
# print(a.upper())

#Remove whitespace: #strip()
# a="Hello, World!"
# print(a.strip())

#Replace string:
# a="Hello, World!"
# print(a.replace("H","J"))

#split string:
# a="Hello, World!"
# print(a.split(",")) #returns ['Hello','World!']

# }concatenation:
#string concatenation:
# a="Hello"
# b="World!"
# c=a+b
# print(c)

#to add a space between them, add a " ":
# a= "Hello"
# b= "world!"
# c= a+" "+b
# print(c)

# }string format
"""the format()method takes the passed arguments, formats them,& are placed 
into the string where the placeholder{} are"""
"""The format()method takes unlimited number of arguments, & 
placed into the respective placeholder"""

# age=36
# txt="My name is John, and I am {}"
# print(txt.format(age))

# quantity=3
# itemno=567
# price=49.95
# myorder="I want {} piece of item {} for {} dollars. "
# print(myorder.format(quantity,itemno,price))

"""you can use index number{0} to be sure the arguments 
are placed in the correst placeholders"""

# quantity=3
# itemno=567
# price=49.95
# myorder="I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity,itemno,price))

# }escape character:
"""to insert characters that are illegal in a string,use an escape character.
an escape character is a backslash(\) followed by the character you want to insert.
an example of an illegal character is a doublequote inside a 
string that is surrounded by doublequotes"""

# txt= "We are the so-called \"Vikings\" from the north."
# print(txt)
'''you will get an error if you use doublequotes inside a string that is surrounded 
by doublequotes'''
# txt="We are the so-called "Vikings" from the north."
# print(txt)

# }Boolean values #Boolean represent one of two values: TRUE or FALSE
#NOTE:when you compare 2 values,the expression is evaluated & python returns the boolean answer
# print(10>9)
# print(10==9) #==:equality operator
# print(10<9)
#NOTE:when you run a condition in an if statement,python returns True or False
# a=200
# b=33

# if b>a:
#     print("b is greater than a")
# else:
#     print("b is not greater than a")
#NOTE:the bool()function allows you to evaluate any value,& give you True or False in return

#evaluate a string & a number:
# print(bool("Hello"))
# print(bool(15))

#evaluate two variables:
# x="Hello"
# y=15

# print(bool(x))
# print(bool(y))
#Most values are True:
'''NOTE:Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list,tuple,set & dictionary are True, except empty ones.'''
#the following will return True:
# bool("abc")
# bool(123)
# bool(["apple","cherry","banana"])
'''NOTE:there are not many values that evaluate to False,except empty values, such as:(),[],{},
"",the number 0, and the value None.And of course the value False evaluates False.'''
# bool(False)
# bool(None)
# bool(0)
# bool("")
# bool(())
# bool([])
# bool({})
'''one more value, or object in this case, evaluates False,and
that is if you have an object that is made from a class 
with a_len_ function that returns 0 or False:'''
# class myclass():
#     def_len_(self):
#     return 0
# myobj=myclass()
# print(bool(myobj))

#Functions can return a boolean
#You can create functions that returns a boolean value:
# def myfunction():
#     return True

# print(myfunction())

'''You can execute code based on the 
boolean answer of a function'''
# def myfunction():
#     return True
# if myfunction():
#     print("Yes!")
# else:
#     print("No!")
'''}the isinstance() function,which can be used 
to determine if an object is of a certain data type:'''
#check if an object is an integer or not:
# x=20
# print(isinstance(x,int))

# x=7
# y=4 #modulus
# print(x%y)

# x=5
# y=2
# print(x**y)#exponentiation

# x=5
# y=1
# print(x^y)
# x=9
# y=2
# print(x&y)
# x=2
# y=3
# print(x|y)
# x=
# y=4
# print(x>>y)
# x=3
# y=11
# print(x<<y)

# }List allows duplicate
# thislist=["apple","banana","cherry","apple","cherry"]
# print(thislist)

# }A list can contain different data types:
# list1=["abc",34,True,40,"male"]
# print(list1)
# list1=["apple","banana","cherry"]
# list2=[1,5,7,9,3]
# list3=[True,False,False]
# print(list1)
# print(list2)
# print(list3)
# print(type(list3))
# thislist=["apple","banana","cherry"]
# print(thislist[-1])
# thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]
# print(thislist[2:5])
# thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]
# print(thislist[:4])
# thislist=["apple","banana","cherry","orange","kiwi","mango"]
# print(thislist[2:])
# thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]
# print(thislist[-4:-1])

# }list length
# thislist=["apple","banana","cherry","watermelon"]
# print(len(thislist))

# }change a range of item value:
# thislist=["apple","banana","cherry","orange","kiwi","mango"]
# thislist[1:3]=["blackcurrant","watermelon"]
# print(thislist)

# thislist=["apple","banana","cherry"]
# thislist[1:3]=["watermelon"]
# print(thislist)
# thislist=["apple","banana","cherry"]
# thislist.insert(2,"watermelon")
# print(thislist)

# }append() method#appends at the end of the list:
# thislist=["apple","banana","cherry"]
# thislist.append("orange")
# print(thislist)
'''}To append elements from another list to the current
list use the extend()method:'''
# thislist=["apple","banana","cherry"]
# tropical=["mango","pineapple","papaya"]
# thislist.extend(tropical)
# print(thislist)

# thislist=["apple","banana","cherry"]
# thistuple=("kiwi","orange")
# thislist.extend(thistuple)
# print(thislist)

# thislist=["apple","banana","cherry"]
# thislist.remove("banana")
# print(thislist)

# }The pop()method removes the specified index:
# thislist=["apple","banana","cherry"]
# thislist.pop(0)
# print(thislist)
#NOTE:if u dont specify the index it will remove the last item.

# }del keyword can also remove the specified index:
# thislist=["apple","banana","cherry"]
# del thislist[0]
# print(thislist)
'''NOTE:you can also delete the entire list completely 
but this will show error'''
# thislist=["apple","banana","cherry"]
# del thislist
# print(thislist)

# }The clear()method this empties the list:
# thislist=["apple","banana","cherry"]
# thislist.clear()#[]
# print(thislist)

# }loop through a list:
# thislist=["apple","banana","cherry"]
# for x in thislist:
#     print(x)

# }loop through the index numbers in list:
# thislist=["apple","banana","cherry"]
# for i in range(len(thislist)):
#     print(thislist[i])

# }using a while loop
# thislist=["apple","banana","cherry"]
# i=0
# while i<len(thislist):
#     print(thislist[i])
#     i=i+1

# }Looping using list comprehension
# thislist=["apple","banana","cherry"]
# [print(x) for x in thislist]
# mylist=["apple","banana","cherry","orange","kiwi","mango"]
# [print(x)for x in mylist]

# }list comprehension:
'''Based on a list of fruits, you want a new list, containing
only the fruits with the letter "a" in the name. NOTE:Without
list comprehension you will have to write a 'for' statement
with a conditional test inside:'''
# fruits=["apple","banana","cherry","kiwi","mango"]
# newlist=[]
# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)
'''NOTE:with list comprehension you can do all that with only
one line of code:'''
# fruits=["apple","banana","cherry","kiwi","mango"]
# newlist=[x for x in fruits if "a"in x]
# print(newlist)

# }condition:
'''the condition is like a filter that only accepts the items
that valuates to True.'''
# fruits=["apple","banana","cherry","orange","kiwi","mango"]
# newlist=[x for x in fruits if x !="apple"]
# print(newlist)

# thistuple=("apple","banana","cherry")
# for i in range(len(thistuple)):
#     print(thistuple[i])
# fruits=("apple","banana","cherry")
# print(len(fruits))



#  }Elif
# a=33
# b=33
# if b>a:
#     print("b is greater than a")
# elif a==b:
#     print("a and b are equal")
# }Else
# a=200
# b=33
# if b>a:
#     print("b is greater than a")
# elif a==b:
#     print("a and b are equal")
# else:
#     print("a is greater than b")

# }CLASS/OBJECT:
# class MyClass:
#     x=6
# p1=MyClass()
# print(p1.x)

# class person:
#     def __init__(self,name,age):
#      self.name=name # ensure you indent as well
#      self.age=age   #make sure you indent here to avoid errror
# p1=person("John",38)

# print(p1.name)
# print(p1.age)

# }OBJECT METHOD:
# class person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age

#     def myfunc(self):
#       print("Hello my name is "+ self.name)

# p1=person("John",36)
# p1.myfunc()

# }MODIFY OBJECTS PROPERTIES:
# class person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age

#     def myfunc(self):
#         print("Hello my name is "+ self.name)

# p1=person("John",36)
# p1.age=40
# print(p1.age)

'''--Parent class is the classs being inherites from, also called BASE CLASS
--Child class is the class that inheritd from another class, also called DERIVED CLASS'''

# }Using Python Inheritance
# :Creating a parent Class
# class person:
#     def __init__(self,fname,lname):
#         self.firstname=fname
#         self.lastname=lname

#     def printname(self):
#         print(self.firstname, self.lastname)
# x=person("John", "Titan")
# x.printname()

# }Creating a child class:
# '''NOTE: to create a class that inherits the functionality from another class 
# send the parent class as a parameter when creating the child class '''

# class person:
#     def __init__(self, fname, lname):
#         self.firstname= fname
#         self.lastname= lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class student(person):
#     pass
# x=student("Mike","Olsen")
# x.printname()

