# You are interested in buying a new laptop. You check the price and you see that the price is 300$ without the 10% tax.

# Create a program that:

# Reads the price of the laptop
# Reads the tax percentage
# Prints the total amount
# Output: "The total price of the laptop is 330$"

# Hieronder verwijdert ge lijn 13 en daar begint ge de logica te schrijven voor het gemiddelde te berekenen en terug te sturen (hint)
# Tip: vergeet niet de logica TERUG te geven...... ;)
def calculateTotalPrice(laptopPrice):
    return(laptopPrice + (laptopPrice*0.1))
  # Ziet er goed uit, wat ook had gekunnen en is iets meer leesbaar:
  # return laptopPrice*1.1


assert calculateTotalPrice(
    300) == 330, "Wrong!  The total laptop price should be 330!"

assert int(calculateTotalPrice(
    850)) == 935, "Wrong! The total laptop price should be 935!"

# nog wat random grote nummers...
assert int(calculateTotalPrice(
    1440)) == 1584, "Wrong! The total laptop price should be 1584!"
print('Everything works!')
