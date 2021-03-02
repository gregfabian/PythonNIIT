# age = 30 
# if age > 16:
#     print("You are old enough to drive")
# else:
#     print("You are not old enough to drive")
# if age >= 21 :
#     print("You are old enough to drive a tractor ")
# elif age >= 16:
#     print("You are old enough to drive a car")
# else:
#     print("You are not old enough to drive")
# if ((age >= 1) and (age < 18)):
#     print("You get a borthday")
# elif(age == 21) or (age >=65):
#     print("You get a birhday")
# elif not(age == 30):
#     print("You don't get a birthday")
# else:
#     print("You get a birthday party yeah")


'''===================================='''
'''for loop '''

# for x in range(0, 10):
#     print(x, ' ', end="")

# print("\n")

'''using a for loop o cycle through a list'''
# grocery_list = ["Juice", "Tomaoes", "Potatoes", "Bananas"]
# for y in grocery_list:
#     print(y)

# for x in [2,4,6,8,10]:
#     print(x)

# num_list = [[1,2,3],[10,20,30],[100,200,330]]
# for x in range(0,3):
#     for y in range(0,3):
#         print(num_list[x][y])

'''Looping Using while loop, while loop is used when you
actually don't have an idea ahead of time how many time you will loop.'''

# import random

# random_num = random.randrange(0, 100)
# while(random_num != 15):
#     print(random_num)
#     random_num = random.randrange(0,100)


'''iterate with while loop like with did with for loop'''
# i = 0
# while(i <= 20):
#     if ((i % 2== 0)):
#         print(i)
#     elif(i == 9):
#         break
#     else:
#         i += 1 # same as i = i + 1
#         continue
#     i += 1


'''+++++++++++++++++++++++++++++++++++++++++++++++++++++'''
'''Using Function'''

# def addNumber(fNum, lNum):
#     sumNum = fNum + lNum
#     return sumNum

# print(addNumber(1, 4))
#or 
# string = addNumber(1, 4)
# print(string)

'''get input from user'''
# import sys

# print("What is your name")
# name = sys.stdin.readline()
# print("Hello", name)

'''dealing with string'''
# long_sring = "I'll catch you if you fall - The Floor"

# print(long_sring[0:4])

# print(long_sring[-5:])

# print(long_sring[:-5])

# print(long_sring[:4] + "be there")

# print("%c is my %s letter and my number %d number is %.5f" %
# ("X", "favorite", 1, .14))

'''capitalize'''

# long_sring = "I'll catch you if you fall - The Floor"
# print(long_sring.capitalize())

# print(long_sring.find("Floor"))

# print(long_sring.isalpha())

# print(long_sring.isalnum())

# print(len(long_sring))

# print(long_sring.replace("Floor","Ground"))

# print(long_sring.split())

# quote_list = long_sring.split(" ")
# print(quote_list)



'''========================================='''

'''File I-O or Input-Output'''
# import os
'''opening a file '''
'''sending wb as ur comman to be able to write to the file'''
# test_file = open("test.txt","wb")


'''outputing the file mode that was beign used which is wb'''
# print(test_file.mode)


'''if you forgot it for some reason and you wanted your files name you type inn name'''
# print(test_file.name)

'''and if you wanted to write txt to a screen or file'''
# test_file.write(bytes("Write me to the file\n", "UTF8"))

'''if you wanted to close a file'''
# test_file.close()

'''open for reading and writing'''
# test_file = open("test.txt", "r+")

# test_in_file = test_file.read()
# print(test_in_file)

'''deleting the file'''
# os.remove("test.txt")



'''============================================='''
''' Objects '''
'''The concept of objects oriented programming allows us to model real world things using code'''
class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height,weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound
    '''By preceeding this variables with two underscores means they will be private'''
    '''To set the name we use def function'''
    '''so we need the use of function, with the use of self'''
    
    def set_name(self, name):
        '''this is to verify the data name in the perenthesis'''
        self.__name = name
    
    def set_height(self, height):
        self.__height = height


    def set_weight(self, weight):
        self.__weight = weight

    def set_sound(self, sound):
        self.__sound = sound


    '''to get name etc.'''
    def get_name(self):
        return self.__name


    def get_height(self):
        return self.__height


    def get_weight(self):
        return self.__weight


    def get_sound(self):
        return self.__sound


    def get_type(self):
        print("Animal")
    
    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {}".format(self.__name,
        self.__height,
        self.__weight,
        self.__sound)

'''creating an object called cat'''
cat = Animal("Whiskers", 33, 10 , "Meow")

print(cat.toString())


'''Inheretance, this means whenever you inherete  from another class that you will automatically get every or all 
the variable and methods or functions that are already created in the class you are inhereting from '''

'''Inherete from animal class for dog'''
class Dog(Animal):
    __owner = ""
    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)


    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {} His owner is {}".format(self.__name,
        self.__height,
        self.__weight,
        self.__sound,
        self.__owner)





    '''To get around method over loading'''
    '''This means you will be able to perform different tasks based of on the attributes that was sent in'''
    def multiple_sounds(self, how_many = None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)
'''creating dog object'''
spot = Dog("Spot", 53, 27, "Ruff", "Greg")

print(spot.toString())

'''polynmophism'''
'''allows you to refere to an object as their super class and then automaticlly have the correct function called automaticaly'''

# class AnimalTesting:
#     def get_type(self, animal):
#         animal.get_type()
# test_animals= AnimalTesting()

# test_animals.get_type(cat)
# test_animals.get_type(spot)

# spot.multiple_sounds(4)
# spot.multiple_sounds()