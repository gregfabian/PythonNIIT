import re
from random import randint

password = input("Enter your password: ")

def pass_verifier(password):
    if len(password) <= 6:
        print("Too Weak, make it stronger")
        return False

    elif len(password) <12:
        if not re.search ("[0-9]",password):
            print("you have to use at least one number in your password")
            return False

        elif not re.search("[a-zA-Z]",password):
            return False

        elif re.search ("[$%!/?>;:</|#@]",password):
            print("Can't use symbols",password)
            return False

        elif re.search ("\s",password):
            print("Avoid whitespaces in your password")
            return False

        else:
            print("Exellent password")
            print("Your password is:",password)
            password2 =input("Comfirm your password: ")
            if password2 != password:
                return False
            else:
                if password2 == password:
                    return True
    else:
        print(password,"must be within range of 6 and 12")    
        return False

    

        
while not pass_verifier(password):
    password = input("Enter your password: ")




print("-------------------------------------------------------------------\n")
print("You are good to go")
print("Use your 5 voucher to play a game")
print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
player_name = input("Hellooooooh!!!,Welcome to the guess game, what is your name? ")
print("Okay!",player_name,"I am Guessing a number between 0 and 5:")

hidden_num = randint(0,5)
print(hidden_num)
bonus = 0
num_of_guesses = 0
guess = 0
total_Bonus = 0

def guess_game(guess,num_of_guesses,hidden_num,bonus,total_Bonus):
    while num_of_guesses < 5:
        guess = int(input("Enter your guess from 0-5: "))
        bonus += 1
        total_Bonus = bonus
        
        
        if guess < hidden_num:
            num_of_guesses += 1
            print("Your guess is too low keep trying")
            print("The number was: ",hidden_num ,"not" ,guess)
            print("You have",(4-num_of_guesses)+1,"guess left")
            print("You have a Bonus of",bonus,"added")
            print("=================================\n")
            
            
        elif guess > hidden_num:
            num_of_guesses += 1
            print("Your guess is too high keep trying")
            print("The number is: ",hidden_num ,"not" ,guess)
            print("You have",(4-num_of_guesses)+1,"guess left")
            print("You have a Bonus of",bonus,"added")
            print("================================\n")
            
        else:
            if guess != hidden_num and num_of_guesses == 5:
                break
    
    if guess == hidden_num:
        print("You guessed the number in",num_of_guesses,"tries!")
        print("The hidden number was :",hidden_num ,"and you guessed",guess," congrats!")
        print("You have a total bonus of: ",total_Bonus)
        print("=================================\n")
        return True
        
    else:
        print("OOps!! Game Over!,you used up your voucher,The number was",hidden_num)
        print("You have a bonus of ",total_Bonus)
        print("*************************************************************\n")
        print("If you wish to continue enter (y) an continue")

            


guess_game(guess,num_of_guesses,hidden_num,bonus,total_Bonus)

to_continue = """
1.      Play game
2.      quit
"""
res = input(to_continue)
while res != "2":
    guess_game(guess,num_of_guesses,hidden_num,bonus,total_Bonus)
    res = input(to_continue)