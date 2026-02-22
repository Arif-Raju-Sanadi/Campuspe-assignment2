#Q4 Age Calculator


#taking birth year from user
birth_year=int(input("Enter your birth year:"))

#taking current year
current_year=2026  

#finding age
age=current_year-birth_year

#calculating other values
age_months=age*12
age_days=age*365
age_hours=age_days*24
age_minutes=age_hours*60

#finding years to become 100
to_100=100-age

# printing result
print("\nYour Age Details:")

print("Age in years:", age)
print("Age in months:", age_months)
print("Age in days:", age_days)
print("Age in hours:", age_hours)
print("Age in minutes:", age_minutes)
print("Years left to become 100:", to_100)