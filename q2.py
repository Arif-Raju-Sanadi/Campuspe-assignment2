#Simple calculator program

#Taking input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

#Addition
add = a+b

#Subtraction
sub = a-b

#Multiplication
mul = a*b

#Division
div=a/b

#Modulus
mod = a%b

#Power
power = a**b

#Printing results
print("\nResults")

print(a, "+", b, "=", add)
print(a, "-", b, "=", sub)
print(a, "*", b, "=", mul)
print(a, "/", b, "=", div)
print(a, "%", b, "=", mod)
print(a, "^", b, "=", power)