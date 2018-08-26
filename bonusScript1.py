# -*- conding: utf8 -*-
import json
import random

def readJSON(file, key):
	values = []
	with open(file) as f:		# 'with' ferme automatiquement le fichier ouvert
		characters = json.load(f)
		for x in characters:
			values.append(x[key])
	return values

def randomCharacter(file):
	characters = readJSON(file, 'character')
	character = characters[random.randint(0, len(characters)-1)]
	return character

print(randomCharacter("characters.json"))