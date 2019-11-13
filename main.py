import argparse
import json

import partie1


def analyser_commande():
    partie1.analyser_commande()

def afficher_damier_ascii(etat_du_jeu):
    matrice = partie1.creation_damier(etat_du_jeu)
    matrice = partie1.afficher_matrice(matrice)
    print(matrice)

