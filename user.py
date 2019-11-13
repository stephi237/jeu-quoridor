
import json
import re

def creation_du_damier():
    # creation du damier
    lignes = 18
    damier = []
    num = 9
    damier.append('Légende: 1=idul, 2=automate')
    for i in range(lignes):   
        if i == 0 :
            damier.append('   ' + '-'*35 )
        elif (i % 2) != 0:
            damier.append(str(num) + ' | ' + '.   '*8 + '. |')
            num = num-1
        else:
            damier.append('  |' +' '*35 + '|') 
    damier.append('--|' + '-'*35 )
    damier.append('  | 1   2   3   4   5   6   7   8   9')


def déchiffrage_du_json(etat_du_jeu):
    data = json.loads(etat_du_jeu)
    joueurs = data["joueurs"]
    j1 = joueurs[0]["pos"]
    j2 = joueurs[1]["pos"]
    murs = data["murs"]
    mh = murs["horizontaux"]
    mv = murs["verticaux"]
    return j1

def positionnement_personnes(damier ,j1):
    #joueur 1
    indiceDamier, indiceChaine = 2*(10-j1[0]), j1[1]*4
    new_chaine = damier[indiceDamier][0:indiceChaine] + '1' + damier[indiceDamier][(indiceChaine+1):len(damier[indiceDamier])]
    damier[indiceDamier] = new_chaine
    print('\n'.join(damier))

etat_du_jeu =  '''{
    "joueurs": [
        {"nom": "idul", "murs": 7, "pos": [5, 5]}, 
        {"nom": "automate", "murs": 3, "pos": [8, 6]}
    ], 
    "murs": {
        "horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]], 
        "verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]]
    }
} '''

if __name__ == "__main__":
    positionnement_personnes( creation_du_damier() ,déchiffrage_du_json(etat_du_jeu))
    

'''def afficher_damier_ascii(etat_du_jeu):
    # creation du damier
    lignes = 18
    damier = []
    num = 9
    damier.append('Légende: 1=idul, 2=automate')
    for i in range(lignes):
        
        if i == 0 :
            damier.append('   ' + '-'*35 )
        elif (i % 2) != 0:
            damier.append(str(num) + ' | ' + '.   '*8 + '. |')
            num = num-1
        else:
            damier.append('  |' +' '*35 + '|') 
    damier.append('--|' + '-'*35 )
    damier.append('  | 1   2   3   4   5   6   7   8   9') 
    
    #déchiffrage de l'état du jeu 
    data = json.loads(etat_du_jeu)
    joueurs = data["joueurs"]
    j1 = joueurs[0]["pos"]
    j2 = joueurs[1]["pos"]
    murs = data["murs"]
    mh = murs["horizontaux"]
    mv = murs["verticaux"]

    #positionnement des joueurs

    #joueur 1
    indiceDamier, indiceChaine = 2*(10-j1[0]), j1[1]*4
    damier[indiceDamier][indiceChaine] = '1'


etat_du_jeu =  '''{
    "joueurs": [
        {"nom": "idul", "murs": 7, "pos": [5, 5]}, 
        {"nom": "automate", "murs": 3, "pos": [8, 6]}
    ], 
    "murs": {
        "horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]], 
        "verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]]
    }
} '''
afficher_damier_ascii(etat_du_jeu )
'''



