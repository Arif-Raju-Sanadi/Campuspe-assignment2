#Q6 Grade Calculator

#taking marks from user
m1=int(input("Enter marks of subject 1: "))
m2=int(input("Enter marks of subject 2: "))
m3=int(input("Enter marks of subject 3: "))
m4=int(input("Enter marks of subject 4: "))
m5=int(input("Enter marks of subject 5: "))

#finding total marks
total=m1+m2+m3+m4+m5

#finding percentage
percent=(total/500)*100

#checking pass or fail
if m1>=40 and m2>=40 and m3>=40 and m4>=40 and m5>=40:
    result="Pass"
else:
    result="Fail"

#deciding grade
if percent>=90:
    grade="A+"
elif percent>=80:
    grade="A"
elif percent>=70:
    grade="B"
elif percent>=60:
    grade="C"
elif percent>=50:
    grade="D"
else:
    grade="F"

#printing result
print("\n=== RESULT ===")

print("Subject 1:",m1)
print("Subject 2:",m2)
print("Subject 3:",m3)
print("Subject 4:",m4)
print("Subject 5:",m5)

print("Total marks:",total)
print("Percentage:",format(percent,".2f"),"%")
print("Grade:",grade)
print("Result:",result)