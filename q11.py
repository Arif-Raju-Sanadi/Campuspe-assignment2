#Q11 Pattern Printing

#showing menu
print("1. Pattern 1")
print("2. Pattern 2")
print("3. Pattern 3")
print("4. Pattern 4")

#taking choice and height
choice=int(input("Enter pattern number: "))
n=int(input("Enter height: "))

#pattern 1
if choice==1:

    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

#pattern 2
elif choice==2:

    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end=" ")
        print()

#pattern 3
elif choice==3:

    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print()

#pattern 4
elif choice==4:

    for i in range(1,n+1):

        #printing left side
        for j in range(1,i+1):
            print(j,end="")

        #printing right side
        for j in range(i-1,0,-1):
            print(j,end="")

        print()

else:
    print("Wrong choice")