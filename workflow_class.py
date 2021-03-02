'''Real World Objects : Attributes & Capabilities
(Fields are basically variables)
(Attributes are called Fields)
Dag Attributes (Fields / Variables) : Height, Weight, Favorite Food
(Methods are basically Functions)
(Capabilities are called Methods)
Dog Capabilities (Methods / Function) : Run, walk, Eat '''

# class Dog:


#     def __init__(self, name="",height=0, weight=0):
#         self.name = name
#         self.height = height
#         self.weight = weight

#     def run(self):
#         print("{} the dog runs".format(self.name))


#     def eat(self):
#         print("{} the dog eats".format(self.name))


#     def bark(self):
#         print("{} the dog barks".format(self.name))

# def main():
#     spot = Dog("Spot", 66, 26)

#     spot.bark()

    
#     bowser = Dog("Bowser")

#     bowser.bark()

# main()

'''Another example: Using getters and setters'''
'''Getters and setter are going to be 
used to protect our objects from 
assigning bad filled values to them or 
also to provide improved output'''

# class Square:

#     def __init__(self, height="0", width="0"):
#         self.height = height
#         self.width = width

#     @property
#     def height(self):
#         print("Retieving the Height")

#         return self.__height

#     @height.setter
#     def height(self, value):
#         if value.isdigit():
#             self.__height = value
#         else:
#             print("Please only enter numbers for height")

#     @property
#     def width(self):
#         print("Retieving the width")

#         return self.__width

#     @width.setter
#     def width(self, value):
#         if value.isdigit():
#             self.__width = value
#         else:
#             print("Please only enter numbers for width")

#     def getArea(self):
#         return int(self.__width) * int(self.__height)

# def main():
#     aSquare =Square()

#     height = input("Enter the Height: ")
#     width = input("Enter the Width: ")
# '''@property and @height and @ with allows us to refer to 
# this values as just height and width, with the property an setup with setter we can just refer to them the way they are and not like : height()'''
#     aSquare.height = height
#     aSquare.width = width


#     print("Height: ", aSquare.height)
#     print("Width: ", aSquare.width)

#     print("The Area is: ", aSquare.getArea())

# main()


