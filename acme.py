#!/usr/bin/python
# -*- coding: utf-8 -*-
import random


class product:

    def __init__(
        self,
        name,
        price=10,
        weight=20,
        flammability=.5,
        identifier=random.randint(1000000, 9999999),
        ):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability_(self):

        stealability = self.weight / self.price
        if stealability < 5:
            return 'not so stealable...'
        elif stealability >= 1:
            return 'Kinda stealable.'
        else:
            return 'Very stealable'

    def explode_(self):
        explode = self.flammability * self.weight
        if explode < 10:
            return '...fizzle'
        elif explode < 50:
            return '....boom!'
        else:
            return '....BABOOM!'


class BoxingGlove(product):

    def __init__(
        self,
        name,
        price=10,
        weight=20,
        flammability=.5,
        identifier=random.randint(1000000, 9999999),
        ):

        super().__init__(name, price, weight, flammability, identifier)

    def explode_(self, explode):
        return '..it\'s a glove'

    def punch_(self):
        if self.weight < 5:
            return '..that tickles'
        elif self.weight >= 5 and self.weight <= 15:
            return '...hey that hurts'
        else:
            return '...OUCH!'
