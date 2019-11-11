import argparse


def analyser_commande():
    parser = argparse.ArgumentParser(description =
    "Permettre l'enregistrement de nouveau joueur et donne l'etat du jeu")
    parser.add_argument( 'idul', type = int, help = 'Idul du joueur')
    
   
    return parser.parse_args()
    