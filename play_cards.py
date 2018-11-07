#!/usr/bin/env python

from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Eliza")

print(d1)

d2 = CardDeck("Aaron")
print(d2)

print(d1.get_dealer())
print(d2.get_dealer())

print(d1.dealer)

d1.dealer = 'Theodosia'

print(d1.dealer)

d2.dealer = 'Alexander'

try:
    d2.dealer = 123.456
except TypeError as err:
    print(err)

print(d2.dealer)

d1.shuffle()
print(d1.cards)

hand = []
for i in range(5):
    hand.append(d1.draw())
print("Hand:", hand)

print(len(d1))
# doing this:
print(CardDeck.__len__(d1))


print(d1)
print(str(d1))

j1 = JokerDeck("Jimmy")
print(j1)
j1.shuffle()
print(j1.cards)




