#Q12 Multiplication Table Generator

#taking number and range from user
num=int(input("Enter number: "))
end=int(input("Enter range (end): "))

#printing table heading
print("\nMultiplication Table of",num)

#loop for table
for i in range(1,end+1):
    result=num*i
    print(num,"x",i,"=",result)