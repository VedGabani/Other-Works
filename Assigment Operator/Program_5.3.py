# Salary Increment

print("----- Salary Increment -----\n")

salary = float(input("Enter current salary: "))
increment_percent = float(input("Enter increment %: "))

increment_amount = (salary * increment_percent) / 100
new_salary = salary + increment_amount

print("Increment Amount:", increment_amount)
print("New Salary:", new_salary)
