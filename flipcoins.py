import random
from decimal import Decimal
from matplotlib import pyplot as plt

# This program simultes flipping coins.
# coins[0] = heads, coins[1] = tails
results = [0, 0]
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
print(f"{results[0]} flips yielded Heads. {results[1]} flips yielded Tails.")
print(f"The probability that {coins} heads in a row will occur is: "\
     f"1 in {sci_notation(pow(2, coins))} or {sci_notation((1 / pow(2, coins)) * 100)} %.")
