#Defining the function for calculations
def Calculator():
    
    #Defining 1st number
    num1=int(input("Enter a number:"))

    #Defining operator
    operator=(input("Enter an operator(+,-,*,/):"))

    #Defining 2nd number
    num2=int(input("Enter a second number:"))

    #if else statement on operators and calculations
    if operator == "+":
        print("Your result is:",(num1 + num2))

    elif operator == "-":
        print("Your result is:",(num1 - num2))

    elif operator == "*":
        print("Your result is:",(num1 * num2))

    elif operator == "/":
        print("Your result is:",(num1 / num2))

    else:
        print(operator,"is not a valid operator")


#defining loop check
def repeat():
    stop = False

    answer = input("Would you like to start another calculation? Please enter y/n: ")
    answer = answer.lower()
    print()

    #no will exit and yes will continue the loop
    while answer !="y" and answer !="n":
        answer = input("please enter y or n: ")
        answer = answer.lower()

    if answer=="n":
        stop = True
        print("Thank you, Have a good day!")

    #exit program
        exit()
        
    return stop


#--MAIN--

#While Loop
stopMain = False

while stopMain == False:

#call calculator function
    Calculator()

#repeat of the program loop check
    repeat()
        
