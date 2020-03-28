import matplotlib.pyplot as plt
from decimal import Decimal
import random

# Randomly draws cards
cards = eval(input("How many cards would you like to draw: "))
diamonds = [0] * 13
clubs = [0] * 13
hearts = [0] * 13
spades = [0] * 13
x = ["Ace", "2", "3", "4", "5", "6", 
"7", "8", "9", "10", "J", "Q", "K"]

for i in range(0, cards):
    suit = random.randint(0, 3)
    rank = random.randint(0, 12)
    if suit == 0:
        diamonds[rank] += 1
    elif suit == 1:
        clubs[rank] += 1
    elif suit == 2:
        hearts[rank] += 1
    elif suit == 3:
        spades[rank] += 1

def sci_notation(num):
    if 2**cards < 10000:
        return num
    return '%.2E' % Decimal(num)

plt.scatter(x, diamonds, label = "Diamonds", color = "darkred")
plt.scatter(x, clubs, label = "Clubs", color = "darkorange")
plt.scatter(x, hearts, label = "Hearts", color = "darkolivegreen")
plt.scatter(x, spades, label = "Spades", color = "darkcyan")

plt.title(f"Results of Drawing {cards} Cards")
plt.xlabel("Rank")
plt.ylabel("Frequency")

plt.legend()
plt.show()

print("Analysis:")
print(f"The probability of drawing the same card {cards} times " \
 f"in a row is 1 in {sci_notation(pow(52, cards))} or " \
  f"{sci_notation((1 / pow(52, cards)) * 100)} %")
