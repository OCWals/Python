# -*- conding: utf8 -*-
from random import randint

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "Vi Veri Veniversum Vivux Vici", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]

def show_random_list(list):
	x = randint(0, 1)
	print(list[x])


for x in characters:
	print(x)

print('')

for x in characters:
	print(x.capitalize())

print('')


user_answer='Y'

while user_answer=='Y':
	show_random_list(quotes)
	user_answer=input("Encore (Y/N) :? ")
