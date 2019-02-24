import math #this imports a package named math which allows us to use the sqrt function

def Menu():  #this is the menu system that repeats on the command Menu()
    print ("\n") #\n creates a new line, an empty new line
    print ("1)Add")
    print ("2)Subtract")
    print ("3)Multiply")
    print ("4)Divide")
    print ("5)Square Root ")

while True:
        Menu()
        print ("\n")
        choice = int(input("Please choose an operation"))
        print ("\n")     
        if choice == 1:
            number1 = float(input("Input 1st Number:"))
            number2 = float(input("Input 2nd Number:"))
            print (number1 + number2) 
        if choice == 2:
            number1 = float(input("Input 1st Number:"))
            number2 = float(input("Input 2nd Number:"))
            print (number1 - number2)
        if choice == 3:
            number1 = float(input("Input 1st Number:"))
            number2 = float(input("Input 2nd Number:"))
            print (number1 * number2)
        if choice == 4:
            number1 = float(input("Input 1st Number:"))
            number2 = float(input("Input 2nd Number:"))
            print (number1 / number2)
        if choice == 5:
            number1 = float(input("Input Number:"))
            print(math.sqrt(number1))
        
