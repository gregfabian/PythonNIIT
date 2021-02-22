# '''John works for 5hrs a day and he works for 5days a week and 
# his rate is 50$/hr, how much does John make in a week'''

# name = input("What is your name? ")
# hoursPer_day = float(input("How many hours do you work in a day? "))
# rate_hour = float(input("How much is your rate per hour "))
# days_week = int(input ("How many days do you work in a week? "))

# daily_wage = hoursPer_day * rate_hour
# weekly_wage = daily_wage * days_week
# print(name,"you earn", weekly_wage,"$ every week." )



password = input("Enter your password: ")
pass_len = len(password)


if pass_len == 0:
    print("You have to enter your password")
elif pass_len > 5 and pass_len <= 10:
    print("Good")
    if "_" in password:
        print("Do not use","_")
elif pass_len <=5:
    print("TOO WEAK")
else:
    print("Error")


# def pass_validator(password):



import re
p= input("Input your password")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")