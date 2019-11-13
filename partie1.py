import argparse
import json

def analyser_commande():
    # analyseur de ligne de commande
    parser = argparse.ArgumentParser(description = 'Jeu Quoridor - phase 1')
    parser.add_argument('idul', help = 'IDUL du joueur.', type = int )
    parser.add_argument('-l', '--lister', metavar = '', help = 
                    'Lister les identifiants de vos 20 dernières parties.')
    return parser.parse_args()

def dechiffrage_du_json(etat_du_jeu):
    # convertit le langage json en objet utilisable
    data = json.loads(etat_du_jeu)
    joueurs = data["joueurs"]
    j1 = joueurs[0]["pos"]
    j2 = joueurs[1]["pos"]
    murs = data["murs"]
    mh = murs["horizontaux"]
    mv = murs["verticaux"]
    info = [j1, j2, mh,mv]
    return info 

def incorporation_element_matrice(matrice, etat_du_jeu ):
    # inserer les elements recupérés de l'état du jeu pour renvoyer le damier correspondant
    [j1, j2, mh,mv] = dechiffrage_du_json(etat_du_jeu) 
    [j1,j2] = traduction_position_joueur([j1,j2])
    mh = traduction_position_murs_horizontaux(mh)
    mv = traduction_position_murs_verticaux(mv)
    for i in mh:
        for j in range(i[1], i[1]+7):
            matrice[i[0]][j] = '-'
    for i in mv:
        for j in range(i[0], i[0]+3):
            matrice[j][i[1]] = '|'
    matrice[j1[0]][j1[1]] = '1'
    matrice[j2[0]][j2[1]] = '2'
    return matrice


def traduction_position_joueur(joueurs ):
    # convertit les coordonnés visuels en coordonnées actuels 
    for i in joueurs:
        i[0], i[1] = 2*(10-i[1]), i[0]*4
    return joueurs

def traduction_position_murs_horizontaux(mh):
    # convertit les coordonnés visuels en coordonnées actuels 
    for i in mh:
        i[0] , i[1] = 2*(10-i[1])+1, 4*i[0]-1
    return mh

def traduction_position_murs_verticaux(mv):
    # convertit les coordonnés visuels en coordonnées actuels 
    for i in mv:
        i[0] , i[1]= 2*(10-i[1])-2, 4*i[0]-2
    return mv



def creation_matrice():
    # creation du plateau de jeu sans joueurs ni murs
    ligne = 21
    colone = 39
    numerotation = 9
    matrice = []
    matrice.append(['Légende: 1=idul, 2=automate'])
    matrice.append(['   -----------------------------------'])
    for i in range(2, ligne-2):
        matrice.append([' ']*39)
    matrice.append(['--|-----------------------------------'])
    matrice.append(['  | 1   2   3   4   5   6   7   8   9'])
    for i in range(2, ligne-2):
        matrice[i][2] = '|'
        matrice[i][38] = '|'
        if (i%2) == 0 :
            matrice[i][0] = str(numerotation)
            numerotation -= 1
            for j in range(1, 10):
                matrice[i][4*j] = '.'
    return matrice


def creation_damier(etat_du_jeu):
    # cree la matrice grâce à l'etat du jeu 
    matrice = creation_matrice()
    incorporation_element_matrice(matrice, etat_du_jeu)
    return matrice


def afficher_matrice(matrice):
    # affiche la matrice sous forme de damier
    for indice, mat1 in enumerate(matrice):
        matrice[indice] = ''.join(mat1)
    return'\n'.join(matrice) 


    






