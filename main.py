import argparse
import json

def analyser_commande():
    # analyseur de ligne de commande
    parser = argparse.ArgumentParser(description = 'Jeu Quoridor - phase 1')
    parser.add_argument('idul', help = 'IDUL du joueur.', type = int )
    parser.add_argument('-l', '--lister', metavar = '', help = 
                    'Lister les identifiants de vos 20 dernières parties.')
    return parser.parse_args()




    


    