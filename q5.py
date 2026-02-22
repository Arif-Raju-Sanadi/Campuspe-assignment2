#Q5 Bill Splitter

#taking inputs from user
bill=float(input("Enter total bill: "))
people=int(input("Number of people: "))
tax_percent=float(input("Tax percentage: "))
tip_percent=float(input("Tip percentage: "))

#subtotal is original bill
subtotal=bill

#finding tax amount
tax_amount=(tax_percent/100)*subtotal

#bill after adding tax
after_tax=subtotal+tax_amount

#finding tip amount
tip_amount=(tip_percent/100)*after_tax

#total bill with tip
total_bill=after_tax+tip_amount

#amount for each person
per_person=total_bill/people

#printing result
print("\n=== BILL BREAKDOWN ===")

print("Subtotal: ₹",format(subtotal,".2f"))
print("Tax (",tax_percent,"%): ₹",format(tax_amount,".2f"))
print("After tax: ₹",format(after_tax,".2f"))
print("Tip (",tip_percent,"%): ₹",format(tip_amount,".2f"))
print("Total: ₹",format(total_bill,".2f"))
print("Per person: ₹",format(per_person,".2f"))