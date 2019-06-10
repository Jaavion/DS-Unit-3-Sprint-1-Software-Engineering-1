#!/usr/bin/python
# -*- coding: utf-8 -*-
# acme_report.py

import random
from acme import product

# Useful to use with random.sample to generate names

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []

    # TODO - your code! Generate and add random products.

    for i in range(0, num_products):
        num = random.randint(0, 4)
        Adjectives = ADJECTIVES[num]
        num = random.randint(0, 4)
        Nouns = NOUNS[num]

        prod = product(Adjectives + ' ' + Nouns, random.randint(5,
                       100), random.randint(5, 100),
                       round(random.uniform(0, 2.5), 2),
                       random.randint(1000000, 9999999))
        products.append(prod)

    return products


  # main program#

def inventory_report(products):
    products_1 = []

    for x in products:
        if x not in products_1:
            products_1.append(x)

    print ('Unique product names: ', len(products_1))
    sum = 0
    for i in products:
        sum += i.price
    mean = sum / len(products)
    print ('Average price:', mean)
    sum = 0
    for i in products:
        sum += i.weight
    mean = sum / len(products)
    print ('Average weight', mean)
    for i in products:
        sum += i.flammability
    mean = sum / len(products)
    print ('Average flammability', mean)


    # len(<list we want to see size of>)

if __name__ == '__main__':
    inventory_report(generate_products())

      
    