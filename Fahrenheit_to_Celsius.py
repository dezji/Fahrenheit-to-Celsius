# Author Name: Deziallia Morris
# Purpose: Convert Fahrenheit to Celsius


# A simple welcome message for the end user with newlines so it is easier to see
print("\nWelcome to the Fahrenheit to Celsius Converter!\n")

# This will gather input from the user and store it in the variable fahrenheit and convert it to an int data type
fahrenheit = int(input("Please enter the temperature in Fahrenheit: "))

# This will process the math and convert the end result into an int data type and store it in the variable
celsius = int((5 / 9) * (fahrenheit - 32))

# This outputs the results in a formatted string
print(f"The current temperature in Celsius is {celsius} degrees.")
