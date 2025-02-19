from listcalculator_module import ListCalculator

# Define a list of numbers
number_list = [1, 2, 3, 4, 5]

# Use the Calculator class from the calculator_module to square the list of numbers
squared_list = ListCalculator.square(number_list)

# Print the result
print("Original List:", number_list)
print("Squared List:", squared_list)