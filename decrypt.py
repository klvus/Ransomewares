#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


fichiers = []

#Obtenir la cle de chiffrement
with open("clechiffrement.key", "rb") as lacle:
	cle = lacle.read()

#Liste des fichiers
for fichier in os.listdir():
	if(os.path.isfile(fichier) and fichier != "darkvador.py" and fichier != "decrypt.py" and fichier != "clechiffrement.key"):
		fichiers.append(fichier)

#Dechiffrement du contenu de chaque fichier

for fichier in fichiers:
	with open(fichier, "rb") as lefichier:
		contenu = lefichier.read()
	contenu_dechiffre = Fernet(cle).decrypt(contenu)
	with open(fichier, "wb") as lefichier:
		lefichier.write(contenu_dechiffre)

print("Congrats, you got your files back")
