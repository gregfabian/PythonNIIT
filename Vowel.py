import re

character = input("Enter a vowel: ")
if  re.search ("[a,e,i,o,u]",character):
    print("vowel sound")
    
elif  re.search ("[A,E,I,O,U]",character):
    print("vowel sound")
    
else:
     print("You entered a consonant",character)

    
        