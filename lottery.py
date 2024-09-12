#Create two empty lists called my_numbers and winning_numbers.

#Loop over a range of 5 steps (i.e., range(0,5)) and populate both lists with a random number between 1 and 69.

#Outside the loop, add one more number to each list that is between 1 and 26.

#Lastly, print the my_numbers and winning_numbers lists to the terminal. The output could look like this:

#My Numbers: [59, 66, 28, 52, 10, 12]
#Winning Numbers: [26, 27, 37, 35, 47, 8]

import random

# Create empty lists
my_numbers = []
winning_numbers = []

# Loop to generate 5 random numbers between 1 and 69
for _ in range(5):
    my_numbers.append(random.randint(1, 69))
    winning_numbers.append(random.randint(1, 69))

# Add one random number between 1 and 26 to each list
my_numbers.append(random.randint(1, 26))
winning_numbers.append(random.randint(1, 26))

# Print the results
print("My Numbers:", my_numbers)
print("Winning Numbers:", winning_numbers)


