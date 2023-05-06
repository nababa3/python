import random
# Generate a random 4-digit number consisting of only 0s and 1s
num = ''.join(random.choices(['0', '1'], k=4))
# Convert the binary number to base 10
decimal_num = int(num, 2)
# Print the generated binary number and its equivalent in base 10
print("Binary number:", num)
print("Decimal equivalent:", decimal_num)