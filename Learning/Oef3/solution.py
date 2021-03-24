# You are interested in buying a new laptop. You check the price and you see that the price is 300$ without the 10% tax.

# Create a program that:

# Reads the price of the laptop
# Reads the tax percentage
# Prints the total amount
# Output: "The total price of the laptop is 330$"

# We breiden uit op de vorige oefening.
# In de vorige oefening was de tax overal 10%
# Nu is er een nieuwe parameter genaamd taxPct
# En wij krijgen in de 3 asserts elke keer een nummer mee dat wij als percentage moeten zien.
# Hoe bouwen we deze functie zodat die code hieronder werkt?

def calculateTotalPrice(laptopPrice, taxPct):
    print('Remove this whole print line and write code here.')


assert calculateTotalPrice(
    300, 10) == 330, "Wrong!  The total laptop price should be 330!"

assert float(calculateTotalPrice(
    850, 21)) == 1028.5, "Wrong! The total laptop price should be 1028.5!"

# nog wat random grote nummers...
assert float(calculateTotalPrice(
    1440, 54)) == 2217.6, "Wrong! The total laptop price should be 2217.6!"
