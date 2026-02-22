#Q7 Temperature Converter

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")

choice=int(input("Enter your choice: "))

temp=float(input("Enter temperature: "))

if choice==1:
    ans=(temp*9/5)+32
    print("Result:",ans)

elif choice==2:
    ans=(temp-32)*5/9
    print("Result:",ans)

elif choice==3:
    ans=temp+273.15
    print("Result:",ans)

elif choice==4:
    ans=temp-273.15
    print("Result:",ans)

elif choice==5:
    ans=(temp-32)*5/9+273.15
    print("Result:",ans)

elif choice==6:
    ans=(temp-273.15)*9/5+32
    print("Result:",ans)

else:
    print("Wrong choice")