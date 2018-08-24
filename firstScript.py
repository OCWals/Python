# -*- conding: utf8 -*-
import random
from turtle import *

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "Vi Veri Veniversum Vivux Vici", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre.",
    "C'est le temps que tu as perdu pour ta rose qui fait ta rose si importante."
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
	x = random.randint(0, len(list)-1)
	print(list[x])


for x in characters:
	print(x)

print('')

for x in characters:
	print(characters.index(x), '. ', x.capitalize())

print('')

user_answer='Y'

while user_answer=='Y':
	show_random_list(quotes)
	user_answer=input("Encore (Y/N) :? ")


print(("{character} a dit : {quote}").format(character="Babar", quote="La vita é bella !"))

def create_message(character, quote):
    print("{} a dit : {}".format(character, quote))

create_message("Wals", "Y'a pas de secret...")

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()