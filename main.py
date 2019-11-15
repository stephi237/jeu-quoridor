import api
import argparse

def analyser_commande():
    # analyseur de ligne de commande
    parser = argparse.ArgumentParser(description = 'Jeu Quoridor - phase 1')
    parser.add_argument('idul', help= 'IDUL du joueur.', type= str )
    parser.add_argument('-l', '--lister',action='store_true' , help= 'Lister les identifiants de vos 20 dernières parties.')
    return parser.parse_args()


def afficher_damier_ascii(etat_du_jeu):
    matrice = api.creation_damier(etat_du_jeu)
    matrice = api.afficher_matrice(matrice)
    print(matrice)

# lancement d'une partie
args = analyser_commande()
if args.lister == True:
    print(api.lister_parties(args))
(identifiant , etat) = api.débuter_partie(args)
start = True
while start == True :
    afficher_damier_ascii(etat)
    print('\t Entre le type de coup que tu veux effectuer -- :')
    print("\t 'D' pour déplacer le jeton \n\t 'MH' pour placer un mur horizontal \n\t ou 'MV' pour placer un mur vertical ")
    type_coup = input()
    position = []
    print('Entre la position (x, y) correspondante')
    position.append(input ('Entre la position x correspondante'))
    position.append(input ('Entre la position y correspondante'))
    etat = api.jouer_coup(identifiant, type_coup ,position)
   

