# Simple Age Checker

# Ask the user for their age
age = int(input("Enter your age: "))

# Check the age category
if age < 18:
    print("You are a minor.")
elif 18 <= age <= 65:
    print("You are an adult.")
elif age > 65:
    print("You are a senior.")
else:
    print("Invalid input. Please enter a valid age.")