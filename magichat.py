#The Sorting Hat is a magical talking hat at Hogwarts School of 
# Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:

#🦁 Gryffindor
#🦅 Ravenclaw
#🦡 Hufflepuff
#🐍 Slytherin
#Write a program that asks the user some questions with the int() and input() functions:

#Q1) Do you like Dawn or Dusk?
 #   1) Dawn
  #  2) Dusk

#If answer is equal to 1, Gryffindor and Ravenclaw both get a +1.
#Else if answer is equal to 2, Hufflepuff and Slytherin both get a +1.
#Else, output the message "Wrong input."
#Q2) When I’m dead, I want people to remember me as:
   # 1) The Good
    #2) The Great
    #3) The Wise
    #4) The Bold

#If the answer is 1, Hufflepuff +2.
#Else if answer is 2, Slytherin +2.
#Else if answer is 3, Ravenclaw +2.
#Else if answer is 4, Gryffindor +2.
#Else, output the message "Wrong input."
#Q3) Which kind of instrument most pleases your ear?
#    1) The violin
#    2) The trumpet
#    3) The piano
#    4) The drum

#If the answer is 1, Slytherin +4.
#Else if the answer is 2, Hufflepuff +4.
#Else if the answer is 3, Ravenclaw +4.
#Else if the answer is 4, Gryffindor +4.
#Else, output "Wrong input."
#Lastly, print out the house with the most points!

# Write code below 💖

import random

print('Welcome to Howarts School of Witchraft and Wizardry!')
print('I am the Sorting Hat, and I will decide wich house you belong to.')
print('Answer the following questions to know your house.')

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

question1 = int(input('Q1) Do you like Dawn or Dusk?\n1 Dawn\n2 Dusk\n '))

if question1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif question1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print('Wrong input.')

question2 = int(input('Q2) When I’m dead, I want people to remember me as:\n1 The Good\n2 The Great\n3 The Wise\n4 The Bold\n'))

if question2 == 1:
    hufflepuff += 2
elif question2 == 2:
    slytherin += 2
elif question2 == 3:
    ravenclaw += 2
elif question2 == 4:
    gryffindor += 2
else:
    print('Wrong input.')

question3 = int(input('Q3) Wich kind of instrument most pleases your ear?\n1 The violin\n2 The trumpet\n3 The piano\n4 The drum\n'))

if question3 == 1:
    slytherin += 4
elif question3 == 2:
    hufflepuff += 4
elif question3 == 3:
    ravenclaw += 4
elif question3 == 4:
    gryffindor += 4
else:
    print('Wrong input.')

houses = {'Gryffindor': gryffindor, 'Ravenclaw': ravenclaw, 'Hufflepuff': hufflepuff, 'Slythering': slytherin}
max_house = max(houses, key=houses.get)
print(f'You belong to {max_house}!')

#The Sorting Hat is a magical talking hat at Hogwarts School of
# Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:



    