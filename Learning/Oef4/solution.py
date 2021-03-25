# Create a program that:

# Given a number, calculate what the sum is of all numbers that are lower than that number
# Example : number = 10. What is the sum of 1+2+3+4+5+6+7+8+9

# Calculates the sum of 1+2+3+4...+98+99
# Give the sum of 1+2+3+4...+98+99
# Output: the sum  of every number below 100 added up is 4950!"


# TIPS
# Bekijk for loops, dat ga je zeker nodig hebben hier.
# https://www.w3schools.com/python/python_for_loops.asp
# Kijk goed naar de range functie op deze page en klik maar op de "Try it yourself" voor wat duidelijkheid... ;)


def calculateTotalSum(number):
    print('Remove this whole print line and write code here.')


assert calculateTotalSum(10) == 45, "Wrong!  The total sum should be 45!"

assert calculateTotalSum(
    100) == 4950, "Wrong!  The total sum should be 4950!"

# nog wat random grote nummers...
assert calculateTotalSum(
    1024) == 523776, "Wrong!  The total sum should be 523776!"
print('Everything works!')