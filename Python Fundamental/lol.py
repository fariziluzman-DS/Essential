#Currency Converter by CodeYourWay
#Download at http://www.codeyourway.co.uk/code/python/example_02.zip

#Defining the code
def main():
    
    #Input the GBP
    GBP = float(input("Enter Pounds: "))

    #Conversion Formulea
    USD = float(GBP * 1.25)
    ERO = float(GBP * 1.11)

    #Allow the user to choose currency of conversion
    Choice = int(input("Would you like to convert to Euros (1) or USD (2)? "))

    #If user selects option 1 (convert to Euros) then
    if Choice == 1:
        print("Euro:")
        print(ERO)

    #If user selects option 2 (convert to USD) then
    elif Choice == 2:
        print("US Dollars:")
        print(USD)

    #If user selects anything other then
    else:
        print("You did not choose a valid option")

    #Looping the code back to the begenning
    Repeat = input("Would you like to run it again? ").lower()
    if Repeat == "yes":
        main()
    else:
        print("Bye")
        exit()

#If you don't add this at the bottom, the code will continuously loop resulting in errors
main()
