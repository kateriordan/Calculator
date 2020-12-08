import random 
print("Welcome to the Tom Nook's store management program 2020 {Kate Riordan} for Nook's Industries")
print("Select one of the following:")
print("[A]: Income Tax Calculator")
print("[B]: Create an Employee Account")
print("[C]: End this Program")

selection = input("Please type in A, B, or C:")

if selection == "A" or selection == "a":
    print("Welcome to the Income Tax Calculator.") 
    income = input("What is your income for the year?")
    while 1:
        try:
            taxedIncome = int(income) * 0.04
            print("With a 4% income tax, you will pay " + str(taxedIncome) + " in taxes this year")
            break 
        except:
            income = input("Please enter an integer value.")
            taxedIncome = int(income) * 0.04
            print("With a 4% income tax, you will pay " + str(taxedIncome) + " in taxes this year")

elif selection == "B" or selection == "b":
    print("Welcome to Employee Account Creation. We will be making your username and password.")
    first = input("Please enter your first name")
    last = input("Please enter your last name")
    print("Your username is " + first[:3] +""+ last[:4] + ".")
    
    passwordBank = ["Fluffy", "Fido", "OneTwoThree", "Honey", "Buddy"]
    randPass = random.choice(passwordBank)
    randNum = random.randint(10,100)
    print("Your password is "+(randPass)+""+str(randNum)+".")
    
elif selection == "C" or selection == "c":
    print("Bye. See you again later.")
    exit

else:
    print("Please enter A, B, or C")
