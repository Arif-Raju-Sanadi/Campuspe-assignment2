#Q8 Leap Year Checker

#taking year from user
year=int(input("Enter a year: "))

#checking leap year conditions
if year%4==0 and (year%100!=0 or year%400==0):
    print(year,"is a Leap Year")
    print("Reason: divisible by 4 and correct century rule")
else:
    print(year,"is NOT a Leap Year")
    print("Reason: does not follow leap year rules")