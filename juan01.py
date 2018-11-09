#!/usr/bin/env python

import barfco.it.johnutil

barfco.it.johnutil.spam()

from barfco.it import johnutil

johnutil.spam()

from barfco.it.johnutil import spam
spam()

from carddeck import CardDeck

d = CardDeck('Louise')
print(d)

import carddeck

d = carddeck.CardDeck('Bob')
print(d)
