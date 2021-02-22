while True:
    numberLine= input("Enter the number: ")
    if type(numberLine) != 'int':
        print("Your number must be an integer")
    else:
        result = numberLine/100
        break
print(result)