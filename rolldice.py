from matplotlib import pyplot as plt
from decimal import Decimal
import random
# Test
# This program simulates rolling a six-sided die.
x = ["One", "Two", "Three", "Four", "Five", "Six"]
y = [0, 0, 0, 0, 0, 0]

rolls = eval(input("Enter how many times you will roll the die: "))
for i in range(0, rolls):
    roll = random.randint(0, 5)
    y[roll] += 1

plt.bar(x, y, color = "goldenrod")
plt.xlabel("Side")
plt.ylabel("Frequency")
plt.title(f"Results of Rolling a Die {rolls} Times")

plt.show()

def sci_notation(num):
    if 6**rolls < 10000:
        return num
    return '%.2E' % Decimal(num)

print("Analysis: ")

sum = 0
for n in y:
    sum += n
def form(n):
    return int(n / sum * 10000) / 100
print(f"One: {form(y[0])}%, Two: {form(y[1])}%, Three: {form(y[2])}%, Four: {form(y[3])}%, Five: {form(y[4])}%, Sox: {form(y[5])}%")
print(f"The probability that {rolls} rolls of one die will land " \
     f"on the same side each time is 1 in {sci_notation(pow(6, rolls))} " \
         f"or {sci_notation((1 / pow(6, rolls)) * 100)} %.")
