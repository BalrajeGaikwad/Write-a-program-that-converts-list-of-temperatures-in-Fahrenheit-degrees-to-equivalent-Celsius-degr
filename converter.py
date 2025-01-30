"""
Write a program that converts list of temperatures in Fahrenheit degrees to equivalent Celsius degrees.
"""

# List of temperatures in Fahrenheit
fahrenheit_temps = [32, 50, 77, 104, 212]

# Convert each temperature to Celsius
for i in range(len(fahrenheit_temps)):
    fahrenheit_temps[i] = (fahrenheit_temps[i] - 32) * 5/9

# Print the result
print("Temperatures in Celsius:", fahrenheit_temps)
