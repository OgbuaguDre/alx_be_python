# pattern_drawing.py

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Outer loop using while to handle rows
while row < size:
    # Inner loop using for to handle columns
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Print newline after each row
    row += 1  # Move to the next row
