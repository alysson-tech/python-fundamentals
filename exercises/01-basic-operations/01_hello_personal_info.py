# Exercise: Enhanced User Introduction
# This script asks the user for their full name, age, and city,
# processes the input, and prints a personalized message with formatted output.

# Ask for the user's full name
full_name = input("Enter your full name: ")

# Loop to validate that the user enters a valid integer for age
while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        # Ask again if the user enters something that's not a number
        print("Please, enter a valid number for your age.")

# Ask for the city where the user lives
city = input("Enter the city where you live: ")

# Format and display the personalized message
# - full_name.split()[0] selects only the first name (before the first space)
# - city.title() capitalizes the first letter of each word in the city
print(f"\n\tHello, {full_name.split()[0]}! You are {age} years old and you live in {city.title()}.")
