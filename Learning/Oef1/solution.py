# It's the end of the semester and you got your grades from three classes: Geometry, Algebra, and Physics.

# Create a program that:

# Reads the grades of these 3 classes (Grades range from 0 - 10)
# Calculate the average of your grades
# Example: Geometry = 6, Algebra = 7, Physics = 8
# Output: average_score = 7


# Hieronder verwijdert ge lijn 14 en daar begint ge de logica te schrijven voor het gemiddelde te berekenen en terug te sturen (hint)
# Tip: vergeet niet de logica TERUG te geven...... ;)
def calculateAverage(grade1, grade2, grade3):
    return((grade1+grade2+grade3)/3)


# Het stukje tekst dat hieronder staat is een assert functie
# Hier gaan we de code uitvoeren : calculateAverage(6,7,8) en de == 7 en bij de andere hetzelfde is de uitkomst dat we verwachten.
# Als de code werkt, dan zie je dat stuke "Wrong! The..." niet meer.
assert calculateAverage(
    6, 7, 8) == 7, "Wrong! The average for (6,7,8) should be 7!"

assert calculateAverage(
    1, 4, 7) == 4, "Wrong! The average for (1, 4, 7) should be 4!"

# nog wat random grote nummers...
assert calculateAverage(
    1546, 7541, 4563) == 4550, "Wrong! The average for (1546, 7541, 4563) should be 4550!"
print('Everything works!')