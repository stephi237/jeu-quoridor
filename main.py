import api
import argparse

# Fonctions du module main

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
start = 0
afficher_damier_ascii(etat)
while start == 0:
    correct = 0
    while (correct == 0):
        print('\t Entre le type de coup que tu veux effectuer -- :')
        print("\t 'D' pour déplacer le jeton \n\t 'MH' pour placer un mur horizontal \n\t ou 'MV' pour placer un mur vertical ")            
        type_coup = input('\t')        
        position = []
        print('Entre la position (x, y) correspondante')        
        position.append(input ('Entre la position x correspondante'))
        position.append(input ('Entre la position y correspondante'))
        try:
            etat = api.jouer_coup(identifiant, type_coup ,position)
            afficher_damier_ascii(etat) 
        except StopIteration:
            print("C'est le gagnant !!!!! :) ")
            start = correct = 1
        except RuntimeError:
            correct = 0
        except :
            correct = 0
        else :
            correct = 1
    
   

