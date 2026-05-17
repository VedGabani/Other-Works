# FunDamental Bosster Program

# Welcome
print("\n")
print("This Program will collect personal information form you")
print("Perform some calculation & Show you data type")
print("Lets get Started\n")

# Information collector

print("\n")

name = input("Enter your name -_- ")
age_str = input("Enter your age -_- ")

# Covert age into int

age = int(age_str)

height_str = input("Enter your height -_- ")

# Covert height into float

height = float(height_str)

fav_str = input("Enter you fav number -_- ")

# Covert fav number into float

fav = float(fav_str)

# Processing

print("\n")
print(f"Your name is {name}")
print(f"You are {age} years old")
print(f"Your height is {height}")
print(f"Your fav number is {fav}\n")

# Calculation

a = int(input("Enter current year -_- "))
b = a - age
sum_value = age + fav
product_value = age * fav
height_cm = height * 100

heights = int(height)
ages = float(age)
age_str = str(age)

# Printing

print(f"Your Born year as per your age is {b} type -_- {type(b)} id -_- {id(b)}")
print(f"Height in int {heights} type -_- {type(heights)} id -_- {id(heights)}")
print(f"Age in flaot {ages} type -_- {type(ages)} id -_- {id(ages)}")
print(f"Age in str {age_str} type -_- {type(age_str)} id -_- {id(age_str)}")

print("\nCalculated result\n")
print(f"Your height in cm {height_cm}cm")
print(f"Sum of you age & fav number {sum_value}")
print(f"Multiplication of your age & fav number {product_value}")

# String concatination

greeting = "Hello, " +name+ "!"
message = f"Your fav number is {fav_str}"
print(f"{greeting} type -_- {type(greeting)} id -_- {id(greeting)}")
print(f"{message} type -_- {type(message)} id -_- {id(message)}")

# Summary Table

print("\nSummary Table\n")

print(f"{'name':<20} {str(name):<20} {str(type(name)):<25} {id(name):<15}")
print(f"{'age':<20} {str(age):<20} {str(type(age)):<25} {id(age):<15}")
print(f"{'fav':<20} {str(fav):<20} {str(type(fav)):<25} {id(fav):<15}")


# Closing message

print("\n\nThank you for using personal data collection")
print("\nYou've successfully explore")
print("\nprint() and input() fn")
print("\nstring , int , float data types")
print("\nAnd many mores")
