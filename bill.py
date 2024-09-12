# List of prices for the meal
bill = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]

# Initialize the total amount to zero
total = 0

# Loop through the bill list to calculate the total amount
for price in bill:
    total += price

# Calculate each person's share by dividing the total by 4
my_share = total / 4

# Print the result
print(f"The total bill is: ${total:.2f}")
print(f"Each person's share is: ${my_share:.2f}")
