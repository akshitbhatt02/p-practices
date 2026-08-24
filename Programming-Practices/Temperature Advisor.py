"""Ask for a temperature in Celsius. 
Convert to Fahrenheit and print a message: "Freezing", "Cold", "Warm", or "Hot" based on ranges. 
Use a function convert(c) and main()."""

                        #   Temperature Advisor

def convert(Celsius):
    F=9/5 * Celsius + 32

    if F <= 32:
        print (F, "is Freezing")
    elif F <= 50:
            print (F, "is Cold")
    elif F <= 68:
            print (F, "is Warm")
    else:
          print (F, "is Hot")

def main():
    while True:
        try: 
            Celsius = int(input("What's the Temperature? (in °C)\n"))  #you have to add loop here for correct value in integer
        except ValueError:
            print("This is an invalid value, Please correct it")
            continue

        convert(Celsius)
        break


main()



