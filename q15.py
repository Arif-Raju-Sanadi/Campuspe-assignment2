#Q15 Prime Number Checker

#part 1 single number
num=int(input("Enter a number: "))

if num<=1:
    print(num,"is NOT a prime number")

else:
    prime=True

    for i in range(2,num):
        if num%i==0:
            prime=False
            break

    if prime==True:
        print(num,"is a PRIME number")
    else:
        print(num,"is NOT a prime number")


#part 2 range
start=int(input("\nEnter start range: "))
end=int(input("Enter end range: "))

print("Prime numbers:")

for n in range(start,end+1):

    if n>1:

        prime=True

        for i in range(2,n):
            if n%i==0:
                prime=False
                break

        if prime==True:
            print(n,end=" ")