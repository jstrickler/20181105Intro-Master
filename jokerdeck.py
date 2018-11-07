#!/usr/bin/env python

from carddeck import CardDeck

#      class    base class
class JokerDeck(CardDeck):

    def _create_deck(self):
        super()._create_deck()  # call parent method
        self._cards.append(('First', 'Joker'))
        self._cards.append(('Second', 'Joker'))
