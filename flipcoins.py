from decimal import Decimal
from matplotlib import pyplot as plt
import random

# This program simulates flipping coins.
results = [0, 0] # [0] = heads, [1] = tails
faces = ["Heads", "Tails"]
coins = eval(input("\nEnter how many coins you will flip: "))
print(f"Flipping {coins} coins...\n")

for i in range(0, coins):
    flip = random.randint(0,1)
    if flip == 0:
        results[0] += 1
    else:
        results[1] += 1

def sci_notation(num):
    if 2**coins < 10000:
        return num
    return '%.2E' % Decimal(num)

plt.bar(faces, results, color = "goldenrod")
plt.xlabel("Side")
plt.ylabel("Frequency")
plt.title(f"Results of Flipping {coins} Coins")
plt.show()

print("Analysis: ")
heads_percentage = sci_notation(results[0] / (results[0] + results[1]) * 100)
print(f"{results[0]} flips yielded Heads. {results[1]} flips yielded Tails. This means ", end = "")
print(f"{float(heads_percentage)} % landed heads, while {100 - float(heads_percentage)} % landed tails")
print(f"The probability that {coins} flips will result in heads in a row is: "\
     f"1 in {sci_notation(pow(2, coins))} or {sci_notation((1 / pow(2, coins)) * 100)} %.")
