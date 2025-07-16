#simple 'if' Statement
#SimpleIfStmtEx1.py
tkt=input("Do u have a Ticket (yes/on):")
if(tkt.lower()=="yes"):
    print("\Enter into theater")
    print("\tEnjoy the moviiee")
    print("\tUnderstand of the message of the moviee")
    print("Goto Home")

#program for accepting a value and decide whether It is Palindrome or Not
#SimpleIfStmtEx2.py
value=input("Enter Any value:")
if(value.upper()==value[::-1].upper()):
    print("{} is palindrome".format(value))
if(value.upper()!=value[::-1].upper()):
    print("{} is Not palindrome.format(value)")
print("program execution completed")

##program for accepting a value and decide whether It is +VE or -VE or Zero
#SimpleIfStmtEx2.py
value=float(input("Enter Any Numerical value:"))#0
if(value>0):
    print("\t{} is +ve".format(value))
if(value<0):
    print("\t{} is -VE".format(value))
if(value==0):
    print("\t{} is ZERO".format(value))
print("program Execution Completed")

#program for accepting any Digit and display its name
#SimpleIfStmtEx4.py
d=int(input("Enter Any Digit:"))#0 1 2 3 4 5 6 7 8 9
if(d==0):
    print("\t{} is ZERO".format(d))
if(d==1):
    print("\t{ is ONE".format(d))
if(d==2):
    print("\t{} is TWO".format(d))
if(d==3):
    print("\t{} is THREE".format(d))
if(d==4):
    print("\t{} is FOUR".format(d))
if(d==5):
    print("\t{} is FIVE".format(d))
if(d==6):
    print("\t{} is SIX".format(d))
if(d==7):
    print("\t{} is SEVEN".format(d))
if(d==8):
    print("\t{} is EIGHT".format(d))
if(d==9):
    print("\t{} is NINE".format(d))
if(d>9):
    print("\t{} is a Number".format(d)) 
if d in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
    print("\t{} is -VE Digit".format(d))
#ifd<0 and d not in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
print("t{} is -VE Number".format(d))
print("program Execution Completed")

#program for accepting a value and decide whether It is +VE or -VE or Zero
#IfElifElseStmtEx1.py                              
value=float(input("Enter Any Numerical Value:")) # 10
if(value>0):
    print("\t{} is +VE Value".format(value))
elif(value<0):
    print("\t{} is -VE Value".format(value))
elif(value==0):
    print("\t{} is ZERO".format(value))
print("Program execution Completed")          
      
#program for accepting any Digit and display its name
#IfElifElseStmtEx2.py
d=int(input("Enter Any Digit:"))# 0  1   2    3  4  5 6 7 8 9
if(d==0):
    print("\t{} is ZERO".format(d))
elif(d==1):
    print("\t{} is ONE".format(d))
elif(d==2):
    print("\t{} is TWO".format(d))
elif(d==3):
    print("\t{} is THREE".format(d))
elif(d==4):
    print("\t{} is FOUR".format(d))
elif(d==5):
    print("\t{} is FIVE".format(d))
elif(d==6):
    print("\t{} is SIX".format(d))
elif(d==7):
    print("\t{} is SEVEN".format(d))
elif(d==8):
    print("\t{} is EIGHT".format(d))
elif(d==9):
    print("\t{} is NINE".format(d))
elif(d>9):
    print("\t{} is a Number".format(d))
elif d in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
    print("\t{} is -VE Digit".format(d))
elif d<0 and d not in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
    print("\t{} is -VE Number".format(d))
print("Program Execution Completed")

#program for accepting any Digit and display its name
#IfElifElseStmtEx2.py
d=int(input("Enter Any Digit:"))# 0  1   2    3  4  5 6 7 8 9
if(d==0):
    print("\t{} is ZERO".format(d))
elif(d==1):
    print("\t{} is ONE".format(d))
elif(d==2):
    print("\t{} is TWO".format(d))
elif(d==3):
    print("\t{} is THREE".format(d))
elif(d==4):
    print("\t{} is FOUR".format(d))
elif(d==5):
    print("\t{} is FIVE".format(d))
elif(d==6):
    print("\t{} is SIX".format(d))
elif(d==7):
    print("\t{} is SEVEN".format(d))
elif(d==8):
    print("\t{} is EIGHT".format(d))
elif(d==9):
    print("\t{} is NINE".format(d))
elif(d>9):
    print("\t{} is a Number".format(d))
elif d in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
    print("\t{} is -VE Digit".format(d))
elif d<0 and d not in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
    print("\t{} is -VE Number".format(d))
print("Program Execution Completed")

#program for accepting a value and decide whether It is Palindrome or Not
#IfElseStmtEx1.py
value=input("Enter Any Value:") # RADAR
if(value.lower()==value[::-1].lower()):
    print("\t{} is Plaindrome".format(value))
else:
    print("\t{} is Not Plaindrome".format(value))
print("Program Execution Completed")

#program for accepting a value and decide whether It is +VE or -VE or Zero
#IfElseStmtEx2.py
value=float(input("Enter Any Numerical Value:")) # 10
if(value>0):
    print("\t{} is +VE Value".format(value))
else:
    if(value<0):
        print("\t{} is -VE Value".format(value))
    else:
        print("\t{} is ZERO".format(value))
    print("Other part of Inner if..else Stmts")
print("Other part of Outer if..else Stmts")

#program for accepting any Digit and display its name
#IfElseStmtEx3.py
d=int(input("Enter Any Digit:"))# 0  1   2    3  4  5 6 7 8 9
if(d==0):
    print("\t{} is ZERO".format(d))
else:
    if (d == 1):
        print("\t{} is ONE".format(d))
    else:
        if (d == 2):
            print("\t{} is TWO".format(d))
        else:
            if (d == 3):
                print("\t{} is THREE".format(d))
            else:
                if (d == 4):
                    print("\t{} is FOUR".format(d))
                else:
                    if (d == 5):
                        print("\t{} is FIVE".format(d))
                    else:
                        if (d == 6):
                            print("\t{} is SIX".format(d))
                        else:
                            if (d == 7):
                                print("\t{} is SEVEN".format(d))
                            else:
                                if (d == 8):
                                    print("\t{} is EIGHT".format(d))
                                else:
                                    if (d == 9):
                                        print("\t{} is NINE".format(d))
                                    else:
                                        if (d > 9):
                                            print("\t{} is a Number".format(d))
                                        else:
                                            if d in [-1, -2, -3, -4, -5, -6, -7, -8, -9]:
                                                print("\t{} is -VE Digit".format(d))
                                            else:
                                                print("\t{} is -VE Number".format(d))
                                                print("program Execution completed")

#program for accepting any Digit and display its name
#IfElseStmtEx3.py
d=int(input("Enter Any Digit:"))# 0  1   2    3  4  5 6 7 8 9
if(d==0):
    print("\t{} is ZERO".format(d))
else:
    if (d == 1):
        print("\t{} is ONE".format(d))
    else:
        if (d == 2):
            print("\t{} is TWO".format(d))
        else:
            if (d == 3):
                print("\t{} is THREE".format(d))
            else:
                if (d == 4):
                    print("\t{} is FOUR".format(d))
                else:
                    if (d == 5):
                        print("\t{} is FIVE".format(d))
                    else:
                        if (d == 6):
                            print("\t{} is SIX".format(d))
                        else:
                            if (d == 7):
                                print("\t{} is SEVEN".format(d))
                            else:
                                if (d == 8):
                                    print("\t{} is EIGHT".format(d))
                                else:
                                    if (d == 9):
                                        print("\t{} is NINE".format(d))
                                    else:
                                        if (d > 9):
                                            print("\t{} is a Number".format(d))
                                        else:
                                            if d in [-1, -2, -3, -4, -5, -6, -7, -8, -9]:
                                                print("\t{} is -VE Digit".format(d))
                                            else:
                                                print("\t{} is -VE Number".format(d))

##program for accepting any Digit and display its name
#DigitEx1.py
d={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}
dig=int(input("Enter Ur Digit:")) # 0 1 2 3 4 5 6 7 8 9
res=d.get(dig) if d.get(dig)!=None else "NUMBER" if (dig > 9) else "-VE DIGIT" if dig in [-1, -2, -3, -4, -5, -6, -7, -8, -9] else "-VE NUMBER"
print("{} is {}".format(dig,res))

##program for accepting any Digit and display its name
#DigitEx2.py
d={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}
dig=int(input("Enter Ur Digit:")) # 0 1 2 3 4 5 6 7 8 9
print("{} is {}".format(dig,d.get(dig) if d.get(dig)!=None else "NUMBER" if (dig > 9) else "-VE DIGIT" if dig in [-1, -2, -3, -4, -5, -6, -7, -8, -9] else "-VE NUMBER"))

#matchcase
#Program for Implementing all Arithmetic Operations by using match case statement
#MatchCaseEx1.py
import sys
print("-"*50)
print("\tArithmetic operations")
print("-"*50)
print("\t\t1.Addition")
print("\t\t2.substraction")
print("\t\t3.Multiplication")
print("\t\t4.Division")
print("\t\t5.Floor Divition")
print("\t\t6.Mod Division")
print("\t\t6.Exponentiataion")
print("\t\t8.Exit")
print("-"*50)
ch=int(input("Enter Ur Choice:"))
match(ch):
    case 1:
        print("Enter Two Values for Addition")
        a,b=float(input()),float(input())
        print("\t\tsum({},{})={}".format(a,b,a+b))
    case 2:
        print("Enter Two Values for Addition")
        a,b=float(input()),float(input())
        print("\t\tsub({},{})={}".format(a,b,a-b))
    case 3:
        print("Enter Two Values for Multiplication")
        a,b=float (input()), float(input())
        print("\t\tMul({},{})={}".format(a,b,a*b))
    case 4:
        print("Enter Two Value for Division")
        a,b=float(input()), float(input())
        print("\t\tDiv({},{})={}".format(a,b,a/b))
    case 5:
        print("Enter Two Values for Floor Div")
        a,b=float(input()), float(input())
        print("\t\tDiv({},{})={}".format(a,b,a//b))
    case 6:
        print("Enter Two Values for Mod Div")
        a,b= float(input()), float(input())
        print("\t\tMod ({},{})={}".format(a,b,a%b))
    case 7:
        a,b= float(input("Enter Base:")), float(input("Enter Power:"))
        print("\t\tpow({},{})={}".format(a,b,a**b)) 
    case 8:
        print("Thx for using program")
        sys.exit() #physical Exit
    case _: 
        print("UR selection of choice is wrong--try again")
        print("program execution is completed")
                                    
def menu():
    print("\n===== Arithmetic Operations Menu =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Modulo Division")
    print("7. Exponentiation")
    print("8. Exit")

def perform_operation(choice, a, b):
    if choice == 1:
        return a + b
    elif choice == 2:
        return a - b
    elif choice == 3:
        return a * b
    elif choice == 4:
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    elif choice == 5:
        if b != 0:
            return a // b
        else:
            return "Error: Floor division by zero"
    elif choice == 6:
        if b != 0:
            return a % b
        else:
            return "Error: Modulo division by zero"
    elif choice == 7:
        return a ** b
    else:
        return "Invalid choice"

while True:
    menu()
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 8:
        print("Exiting the program. Goodbye!")
        break

    if choice in [1, 2, 3, 4, 5, 6, 7]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = perform_operation(choice, num1, num2)
            print("Result:", result)
        except ValueError:
            print("Please enter valid numbers.")
    else:
        print("Invalid choice. Please try again.")

import math

def menu():
    print("\n===== Area Calculator Menu =====")
    print("C. Circle")
    print("R. Rectangle")
    print("S. Square")
    print("T. Triangle")
    print("E. Exit")

def area_of_circle():
    r = float(input("Enter radius of the circle: "))
    return math.pi * r * r

def area_of_rectangle():
    l = float(input("Enter length of the rectangle: "))
    b = float(input("Enter breadth of the rectangle: "))
    return l * b

def area_of_square():
    s = float(input("Enter side of the square: "))
    return s * s

def area_of_triangle():
    b = float(input("Enter base of the triangle: "))
    h = float(input("Enter height of the triangle: "))
    return 0.5 * b * h

while True:
    menu()
    choice = input("Enter your choice: ").upper()

    if choice == 'C':
        print("Area of Circle:", area_of_circle())
    elif choice == 'R':
        print("Area of Rectangle:", area_of_rectangle())
    elif choice == 'S':
        print("Area of Square:", area_of_square())
    elif choice == 'T':
        print("Area of Triangle:", area_of_triangle())
    elif choice == 'E':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

def menu():
    print("\n===== Temperature Conversion Calculator =====")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Fahrenheit")
    print("6. Kelvin to Celsius")
    print("7. Exit")

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def kelvin_to_celsius(k):
    return k - 273.15

while True:
    menu()
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        c = float(input("Enter temperature in Celsius: "))
        print("Temperature in Fahrenheit:", celsius_to_fahrenheit(c))

    elif choice == 2:
        c = float(input("Enter temperature in Celsius: "))
        print("Temperature in Kelvin:", celsius_to_kelvin(c))

    elif choice == 3:
        f = float(input("Enter temperature in Fahrenheit: "))
        print("Temperature in Celsius:", fahrenheit_to_celsius(f))

    elif choice == 4:
        f = float(input("Enter temperature in Fahrenheit: "))
        print("Temperature in Kelvin:", fahrenheit_to_kelvin(f))

    elif choice == 5:
        k = float(input("Enter temperature in Kelvin: "))
        print("Temperature in Fahrenheit:", kelvin_to_fahrenheit(k))

    elif choice == 6:
        k = float(input("Enter temperature in Kelvin: "))
        print("Temperature in Celsius:", kelvin_to_celsius(k))

    elif choice == 7:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

      