#Keep asking for age until the user enters a valid positive integer (use try/except). 
#Then print whether they're a minor, adult, or senior (conditionals).

while True:
    try :
        age = int(input("Enter your age: "))
        if age < 1:
            print("Please enter a positive number")
            continue
        if age < 18:
            print("You are Minor.")
        elif age < 35:
            print("You are Adult.")
        elif age < 55:
            print("You are Senior, sir.")
        else :
            print("Hello, Very Senior Citizen. Welcome!!")
        break
    except ValueError:
        print("Please Enter a valid number")
        continue #this conitune is only for the except block, so that if the user enters a non-integer value, it will prompt them to enter a valid number again without breaking the loop.
    