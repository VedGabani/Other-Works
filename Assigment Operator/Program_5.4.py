# Disscount Calculation

print("----- Disscount Calculation -----\n")

price = float(input("Enter original price -_- "))
discount_percent = float(input("Enter discount % -_- "))

discount_amount = (price * discount_percent) / 100

price -= discount_amount
print("Discount Amount -_- ", discount_amount)
print("Final Price -_- ", price)
