#Q13 Sum and Average Calculator
#taking how many numbers
n=int(input("How many numbers? "))

#initial values
total=0

#taking first number to set max and min
first=int(input("Enter number 1: "))
total=total+first
max_num=first
min_num=first

#loop for remaining numbers
for i in range(2,n+1):

    num=int(input("Enter number "+str(i)+": "))
    total=total+num

    #checking max
    if num>max_num:
        max_num=num

    #checking min
    if num<min_num:
        min_num=num

#finding average
avg=total/n

#printing result
print("\nSum:",total)
print("Average:",avg)
print("Maximum:",max_num)
print("Minimum:",min_num)