#Q9 Ticket Pricing System

#taking inputs from user
age=int(input("Enter your age: "))
day=input("Enter day of week: ")
tickets=int(input("Enter number of tickets: "))

#finding base price by age
if age<3:
    price=0
elif age>=3 and age<=12:
    price=150
elif age>=13 and age<=59:
    price=300
else:
    price=200

#finding total without discount
base_total=price*tickets

#checking discount days
day=day.lower()

if day=="friday" or day=="saturday" or day=="sunday":
    discount=0.20*base_total
else:
    discount=0

#price after discount
after_discount=base_total-discount

#printing result
print("\n=== TICKET DETAILS ===")

print("Base price per ticket: ₹",price)
print("Total without discount: ₹",base_total)
print("Discount: ₹",discount)
print("After discount: ₹",after_discount)
print("Total amount: ₹",after_discount)