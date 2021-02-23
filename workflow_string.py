# rand_string = "    this is an important string    "
# rand_string = rand_string.lstrip()

# rand_string = rand_string.rstrip()

# rand_string = rand_string.strip()

# print(rand_string.capitalize())

# print(rand_string.upper())

# print(rand_string.lower())
# a_list = ["Bunch", "of", "random", "words"]
# print(" ".join(a_list))

# a_list_2 = rand_string.split()
# for i in a_list_2:
#     print(i)

# print("How many is: ", rand_string.count("is"))
# print("Where is string: ", rand_string.find("string"))
# print(rand_string.replace("an ", "a kind of "))


'''==============================='''
'''Random Access Memory: RAM'''
#Ask for a string
orig_string = input("Convert to Acronym: ")

#Convert the string to uppercase
orig_string = orig_string.upper()


#Convert the string into a list
list_of_words = orig_string.split()

# Cycle through the list 
for word in list_of_words:

    #Get the first letter of the word abd eliminate the newline
    print(word[0], end="")

#Add a newline
print()

'''Additional methods'''
# letter_z = "z"
# num_3 = "3"
# a_space = " "

# print("Is z a letter or number: ", letter_z.isalnum())

# print("Is z a letter: ", letter_z.isalnum())

# print("Is 3 a number: ", num_3.isalnum())

# print("Is z a lowercase: ", letter_z.islower())

# print("Is z a upper: ", letter_z.isupper())

# print("Is space a space: ", a_space.isspace())

'''Additional methods using a function to avoid repeating a code'''
# letter_z = "z"
# num_3 = "3.14"
# a_space = " "

# def isfloat(str_val):
#     try:
#         float(str_val)
#         return True
#     except ValueError:
#         return False
# '''calling our function'''
# print("Is pi a float: ",isfloat(num_3))

''' implementing ceaser cypher inside of a program passing a message you want to be encrypted'''
'''Unicode'''
#A - Z 65-90
#a - z 97 - 122
#ord(your_letter)
#chr(your_code)

#Hints
#Use isupper()to decide which unicode to work with 
#Add rthe key (number of characters to shift) and if 
#the key is bigger or smaller than the unicode for 
#A,Z,a,z increase or decrease by 26

#receive the message to encrypt and the number of
#characters to shift
message = input("Enter your message: ")
key = int(input("How many characters should we shift (1-26): "))

#prepare the secret_message
secret_message = ""

#Cycle through each character in the message
for char in message:

    #If it isn't a letter then keep it as it is 
    if char.isalpha():
        #Get the character code and add the shift amount
        char_code = ord(char)
        char_code += key
        #If upppercase then compare to uppercase unicodes
        if char.isupper():
            #If bigger then Z subtract 26 
            if char_code > ord("Z"):
                char_code -= 26
            #If smaller than A add 26
            if char_code < ord("A"):
                char_code += 26
    #Do the same for lowercase characters
        else:
            if char_code > ord("z"):
                char_code -= 26
            if char_code < ord("a"):
                char_code += 26
    #Convert from code to letter and add to message 
        secret_message += chr(char_code)
    else:
        secret_message += char

print("Encrypted: ",secret_message)

key = - key

orig_message = ""

#Cycle through each character in the message
for char in secret_message:

    #If it isn't a letter then keep it as it is 
    if char.isalpha():


        #Get the character code and add the shift amount
        char_code = ord(char)
        char_code += key


        #If upppercase then compare to uppercase unicodes
        if char.isupper():

            #If bigger then Z subtract 26 
            if char_code > ord("Z"):
                char_code -= 26

            #If smaller than A add 26
            if char_code < ord("A"):
                char_code += 26

    #Do the same for lowercase characters
        else:
            if char_code > ord("z"):
                char_code -= 26
            if char_code < ord("a"):
                char_code += 26

    #Convert from code to letter and add to message 
        orig_message += chr(char_code)
    else:
        orig_message += char

print("Decrypted: ",orig_message)