#Create a currency.py program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.

pesos = float(input('Enter the amounth of pesos you have: '))
soles = float(input('Enter the amonunt of soles you have:' ))
reis = float(input('Enter the amounth of reis you have: '))
usd = pesos/20.31 + soles/3.95 +reis/5.77
print(f'You have {usd} USD')

# The program should ask the user for the amount they have in each currency and then display the total in USD.
