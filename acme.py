class product:
    def __init__(self, name, price, weight, flammability, identifier,stealability, explode):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self. identifier = identifier
    #def product_(self):
        #print(self.name)
       # print(self.price)
       # print(self.weight)
       # print(self.flammability)
      #  print(self.identifier)
        self.stealability = stealability
        self.explode = explode
	
	def dangers(self):
        if self.stealability < 0.5:
            print('Not so stealable')
        elif self.explode >= 10 and < 50:
            print('...fizzle.')
        else:
        	print('..BABOOM')
class BoxingGlove():
  	def __init__(self, punch):
        self.puncj = punch
    	super().__init__(self, name, price, weight, flammability, identifier, stealability, explode)
    def dangers(self):
        if self.stealability < 0.5:
            print('Not so stealable')
        elif self.explode >= 10 and < 50:
            print('...fizzle.')
        else:
        	print('..BABOOM')

import random
acnme = product(name=None, price = 10, weight = 20, flammability = 0.5, identifier = random.randint(1000000, 9999999), stealability = price/weight, explode = flammability * weight)
acnme_dangers = product(name=None, price = 10, weight = 20, flammability = 0.5, identifier = random.randint(1000000, 9999999), stealability = price/weight, explode = flammability * weight)
acme_boxing_glove = BoxingGlove(name=None, price = 10, weight = 10, flammability = 0.5, identifier = random.randint(1000000, 9999999), stealability = price/weight, explode = 'it/s a glove', punch = 'that tickles')



