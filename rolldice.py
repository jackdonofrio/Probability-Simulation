from matplotlib import pyplot as plt
from decimal import Decimal
import random

# This program simulates rolling a six-sided die.
x = ["One", "Two", "Three", "Four", "Five", "Six"]
y = [0, 0, 0, 0, 0, 0]

rolls = eval(input("Enter how many times you will roll the die: "))
for i in range(0, rolls):
    roll = random.randint(0, 5)
    y[roll] += 1

def sci_notation(num):
    if 6**rolls < 10000:
        return num
    return '%.2E' % Decimal(num)

plt.bar(x, y, color = "goldenrod")
plt.xlabel("Side")
plt.ylabel("Frequency")
plt.title(f"Results of Rolling a Die {rolls} Times")

plt.show()

print("Analysis: ")
print(f"The probability that {rolls} rolls of one die will land " \
     f"on the same side each time is 1 in {sci_notation(pow(6, rolls))} " \
         f"or {sci_notation((1 / pow(6, rolls)) * 100)} %.")
