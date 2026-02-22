#Q18 Calculator Functions

#function for addition
def add(a,b):
    return a+b

#function for subtraction
def subtract(a,b):
    return a-b

#function for multiplication
def multiply(a,b):
    return a*b

#function for division
def divide(a,b):
    if b==0:
        return "Cannot divide by zero"
    else:
        return a/b

#function for modulus
def modulus(a,b):
    return a%b

#function for power
def power(a,b):
    return a**b


#main calculator function
def calculator():

    while True:

        print("\n--- CALCULATOR ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice=int(input("Enter choice: "))

        if choice==7:
            print("Exit from calculator")
            break

        a=float(input("Enter first number: "))
        b=float(input("Enter second number: "))

        if choice==1:
            print("Result:",add(a,b))

        elif choice==2:
            print("Result:",subtract(a,b))

        elif choice==3:
            print("Result:",multiply(a,b))

        elif choice==4:
            print("Result:",divide(a,b))

        elif choice==5:
            print("Result:",modulus(a,b))

        elif choice==6:
            print("Result:",power(a,b))

        else:
            print("Wrong choice")


#calling main function
calculator()