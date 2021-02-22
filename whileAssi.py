import re

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
            if password == password2:
                print("You are good to go")
                start_game = ("Use your 5 voucher to play a game")
                if password == password2:
                    print(start_game)
                    print(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
            return True
            
    else:
        print(password,"must be within range of 6 and 12")    
        return False

    

        
while not pass_verifier(password):
    password = input("Enter your password: ")



from random import randint


player_name = input("Hellooooooh!!!,Welcome to the guess game, what is your name? ")
print("Okay!",player_name,"I am Guessing a number between 0 and 5:")

hidden_num = randint(0,5)
Bonus= 0
num_of_guesses = 0

while num_of_guesses < 5:
    guess = int(input("Enter your guess: "))
    Bonus +=1
    Total_Bonus = Bonus
    num_of_guesses += 1


    if guess < hidden_num:
        print("Your guess is too low keep trying")
        print("You have",5-(num_of_guesses),"guess left")
        print("You have a Bonus of",(Bonus),"added")
        print("=================================\n")

    elif guess > hidden_num:
        print("Your guess is too high keep trying")
        print("You have",5-(num_of_guesses),"guess left")
        print("You have a Bonus of",(Bonus),"added")
        print("================================\n")

    else: 
        if guess != hidden_num and num_of_guesses == 5:
            break

if guess == hidden_num:
    print("You guessed the number in",num_of_guesses,"tries!")
    print("You have a total bonus of: ",Total_Bonus)
    print("=================================\n")


else:
    print("OOps!! Game Over!,you used up your voucher,The number was",hidden_num)
    print("You have a bonus of ",Total_Bonus)
    print("*************************************************************\n")
   

pass_verifier(password)