# def my_bmi():
#     weight = int(input("Enter your weight in kilogram: "))
#     height = int(input("Enter your height in meter"))
#     bmi = (weight) / (height*height)

#     if (bmi <16):
#         return bmi

# result = my_bmi
# print(result)


# def fnname(a, b, c):
#     a = 1
#     return a

# fnname()

# # '''#$ASSIGNMENT:'''
# #===================================================

def my_bmi():
    name = input("Enter your name: ")
    weight= int(input("Enter your weight in kilogram: "))
    height= int(input("Enter your height centimeter: "))
    conv_to_meter= height/100
    bmi=weight/(conv_to_meter**2)
    print(name,"Your bmi is:",bmi, "you are: ",end=" ")   
    

def veganism(bmi):
    if (bmi < 16):
        print("severely underweight")
        weight_status= (input("Enter your weight_status: "))
        if weight_status.lower() == ("severely underweight"):
            print("You will have to engage in a veganism")
            time = input("Enter time: ")
            if time.lower() == ("morning"):
                print(f"""8:30am""")
                print("you will take vegetables,boiled eggs and fruits in the morning")
            elif time.lower() == ("afternoon"):
                print(f"""2:30pm""")
                print("you will take cheese,egg-free parta and milk in the afternoon")
            elif time.lower() == ("evening"):
                print(f"""5:30pm""")
                print("you will eat either of this beans, legumes, and grains with fruits an vegetables")
            else:
                print("Invalid input")
                      

def carnivore_diet():
    carnivore_diet
    if (bmi >= 16 and bmi <= 18.5):
        print("underweight")
        weight_status= input("Enter your weight_status: ")
        if weight_status.lower() == ("underweight"):
            print("you will have to be on a carnivore diet")
            time = input("Enter time: ")
            if time.lower() == ("morning"):
                print(f"""8:30am""")
                print("you will take meat, cheese milk and boiled egg in the morning")
            elif time.lower() == ("afternoon"):
                print(f"""2:30pm""")
                print("you will take beans and vegetables in the afternoon")
            elif time.lower() == ("evening"):
                print(f"""5:30pm""")
                print("you will take bunless cheeseburgers,fried plantain, and avocados in the evening")
            else:
                print("Invalid input")
            

def sirtfood_diet():
    sirtfood_diet
    if (bmi >= 18.5 and bmi <=24.9):
        print("Healthy weight") 
        weight_status= input("Enter your weight_status: ")
        if weight_status.lower() == ("healthy weight"):
            print("you will have to be on a sirtfood diet")
            time = input("Enter time: ")
            if time.lower() == ("morning"):
                print(f"""8:30am""")
                print("you will take walnuts and coffee")
            elif time.lower == ("afternoon"):
                print(f"""2:30pm""")
                print("you will take medjool dates, capers and extra-virgin olive oil")
            elif time.lower == ("evening"):
                print(f"""5:30pm""")
                print("you will take fried plantain and beans or vegetables and fruits")
            else:
                print("Invalid input")
            
def paleo_diet():
    paleo_diet
    if (bmi >= 24.9 and bmi <= 29.9):
        print("overweight")
        weight_status= input("Enter your weight_status: ")
        if weight_status.lower() == ("overweight"):
            print("You will have to be on a paleo diet")
            time = input("Enter time: ")
            if time.lower() == ("morning"):
                print(f"""5:30am""")
                print("NOTE:make sure you excercise early morning before intake of anything")
                print("you will take vegetables and fruits")
            elif time.lower() == ("afternoon"):
                print(f"""2:30pm""")
                print("you will take fruits and cheese")
            elif time.lower() == ("evening"):
                print(f"""5:30pm""")
                print("you will take fruits")
                print("always avoid processed foods please")
            else:
                print("Invalid input")
            

def ketogenic_diet():
    ketogenic_diet
    if (bmi >= 30.0):
        print("obese")
        weight_status= input("Enter your weight_status: ")
        if weight_status.lower() == ("obese"):
            print("You will have to be on a Ketogenic diet")
            time = input("Enter time: ")
            if time.lower() == ("morning"):
                print(f"""4:30am""")
                print("Go and excercise for like five hours first thing in the morning then,",end="")
                print("you will take vegetables and fruits after your excercise")
            elif time.lower() == ("afternoon"):
                print(f"""2:30pm""")
                print("you have to excercise,",end="")
                print("after your excercise you take enough water and fruits")
            elif time.lower() == ("evening"):
                print(f"""5:30pm""")
                print("you will take bunless cheeseburgers and a lot of avocados")
    
my_bmi()
veganism(bmi)
carnivore_diet()
sirtfood_diet()
paleo_diet()
ketogenic_diet()


# import platform
# x=platform.system()
# print(x)

# import platform
# x = dir(platform)
# print(x)

# def bmi_calculator():
#     name = input("Enter your name: ")
#     age = input("Enter your age: ")
#     height = int(input("Enter your height in centimeter: "))
#     weight = int(input("Enter your weight in meter: "))
#     conv_to_meter= height/100
#     bmi= weight/(conv_to_meter**2)
#     return bmi

# bmi = bmi_calculator()
# if (bmi < 16):
#     print("severely underweight")
#     weight_status= (input("Enter your weight_status: "))
#     if weight_status.lower() == ("severely underweight"):
#         print("You will have to engage in a veganism")
#         time = input("Enter time: ")
#         if time.lower() == ("morning"):
#             print(f"""8:30am""")
#             print("you will take vegetables,boiled eggs and fruits in the morning")
#         elif time.lower() == ("afternoon"):
#             print(f"""2:30pm""")
#             print("you will take cheese,egg-free parta and milk in the afternoon")
#         elif time.lower() == ("evening"):
#             print(f"""5:30pm""")
#             print("you will eat either of this beans, legumes, and grains with fruits an vegetables")
#         else:
#             print("Invalid input")
                      
# elif (bmi >= 16 and bmi <= 18.5):
#     print("underweight")
#     weight_status= input("Enter your weight_status: ")
#     if weight_status.lower() == ("underweight"):
#         print("you will have to be on a carnivore diet")
#         time = input("Enter time: ")
#         if time.lower() == ("morning"):
#             print(f"""8:30am""")
#             print("you will take meat, cheese milk and boiled egg in the morning")
#         elif time.lower() == ("afternoon"):
#             print(f"""2:30pm""")
#             print("you will take beans and vegetables in the afternoon")
#         elif time.lower() == ("evening"):
#             print(f"""5:30pm""")
#             print("you will take bunless cheeseburgers,fried plantain, and avocados in the evening")
#         else:
#             print("Invalid input")
            
# elif (bmi >= 18.5 and bmi <=24.9):
#     print("Healthy weight") 
#     weight_status= input("Enter your weight_status: ")
#     if weight_status.lower() == ("healthy weight"):
#         print("you will have to be on a sirtfood diet")
#         time = input("Enter time: ")
#         if time.lower() == ("morning"):
#             print(f"""8:30am""")
#             print("you will take walnuts and coffee")
#         elif time.lower == ("afternoon"):
#             print(f"""2:30pm""")
#             print("you will take medjool dates, capers and extra-virgin olive oil")
#         elif time.lower == ("evening"):
#             print(f"""5:30pm""")
#             print("you will take fried plantain and beans or vegetables and fruits")
#         else:
#             print("Invalid input")
        
# elif (bmi >= 24.9 and bmi <= 29.9):
#     print("overweight")
#     weight_status= input("Enter your weight_status: ")
#     if weight_status.lower() == ("overweight"):
#         print("You will have to be on a paleo diet")
#         time = input("Enter time: ")
#         if time.lower() == ("morning"):
#             print(f"""5:30am""")
#             print("NOTE:make sure you excercise early morning before intake of anything")
#             print("you will take vegetables and fruits")
#         elif time.lower() == ("afternoon"):
#             print(f"""2:30pm""")
#             print("you will take fruits and cheese")
#         elif time.lower() == ("evening"):
#             print(f"""5:30pm""")
#             print("you will take fruits")
#             print("always avoid processed foods please")
#         else:
#             print("Invalid input")
            
# elif (bmi >= 30.0):
#     print("obese")
#     weight_status= input("Enter your weight_status: ")
#     if weight_status.lower() == ("obese"):
#         print("You will have to be on a Ketogenic diet")
#         time = input("Enter time: ")
#         if time.lower() == ("morning"):
#             print(f"""4:30am""")
#             print("Go and excercise for like five hours first thing in the morning then,",end="")
#             print("you will take vegetables and fruits after your excercise")
#         elif time.lower() == ("afternoon"):
#             print(f"""2:30pm""")
#             print("you have to excercise,",end="")
#             print("after your excercise you take enough water and fruits")
#         elif time.lower() == ("evening"):
#             print(f"""5:30pm""")
#             print("you will take bunless cheeseburgers and a lot of avocados")




# def isFiveCharacters(inputString):
#     while len(inputString) > 5:
#         return True #print('Contains at least 5 characters, ')
#     else:
#         print('Invalid! Password must cantain more than 5 characters')
#     return False
# def hasUpperCase(inputString):
#     x = any(char.isupper() for char in inputString)
#     if x == True:
#         return True #print ('an uppercase letter, ')
#     if x == False:
#         print('Invalid! Password must contain an upper case letter')
#     return False
# def hasNumbers(inputString):
#     count = 0
#     for char in inputString:
#         if char == char.isdigit():
#             count += 1
#             if count >= 2:
                # print ('two numbers, ')
#                 return True
#             elif count < 2:
#                 print ('Invalid! Password must contain two numbers')
#                 return False
# def hasLetterE(inputString):
#     for char in inputString:
#         if 'E' and 'e' in inputString:
#             print('Invalid! Password cannot contain the letter "E"')
#             return False
        # else:
            #print('does not contain the letter E, ')
            # return True
    #if 'e' in inputString:
#        print('Password cannot contain the letter "e"')
#    return None
# def nonAlphaNumChar(inputString):
#     special_char = ['!','@','$','%','#','^','&','*']
#     if inputString == special_char * 2:
            #print('a special character, ')
#         return True
#     else:
#         print('Invalid! Password must contain a special character')
#     return None
# def usedPasswords(inputString):
#     used_passwords = ('password','12345','qwerty','letmein','trustno1','000000','passw0rd','Password')
#     if used_passwords == inputString:
#         print('Invalid! Password must be original.')
#         return False
# def passwordCriteria(inputString):
#     isFiveCharacters(inputString)
#     hasUpperCase(inputString)
#     hasNumbers(inputString)
#     hasLetterE(inputString)
#     nonAlphaNumChar(inputString)
#     usedPasswords(inputString)
#     while inputString == True:
#         print('Valid Password')
#         return True
#     if inputString == False:
#         print('Error, invalid password')
#         return False
#     return None



