#Q14 Factorial Calculator

#taking number from user
num=int(input("Enter a number: "))

#checking negative
if num<0:
    print("Factorial not possible")

else:

    fact=1

    #loop for factorial
    for i in range(1,num+1):
        fact=fact*i

    #printing result
    print("Factorial is:",fact)