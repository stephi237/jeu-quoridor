class QuoridorError(Exception):
    pass


class Quoridor():

    def __init__(self, joueurs, murs=None):
        # si joueurs n'est pas itérable
        if(not isinstance(joueurs, list)) or (not isinstance(joueurs, tuple)):
            raise QuoridorError

        # si l'itérable de joueurs en contient plus de deux.
        if(len(joueurs) != 2):
            raise QuoridorError

        # si le nombre de murs qu'un joueur peut placer est >10, ou négatif
        for joueur in joueurs:
            if(isinstance(joueur, dict)):
                if joueur['murs'] > 10 or joueur['murs'] < 0:
                    raise QuoridorError

                # si la position d'un joueur est invalide
                for coord_pos in joueur['pos']:
                    if not (coord_pos in range(1, 10)):
                        raise QuoridorError

        # si murs n'est pas un dictionnaire lorsque présent.
        if(murs != None and not(isinstance(murs, dict))):
            raise QuoridorError

        # si le total des murs placés et plaçables n'est pas égal à 20
        count = 0
        if(murs == None):
            for joueur in joueurs:
                if(isinstance(joueur, str)):
                    count += 10
                else:
                    count += joueur['murs']
        else:
            for joueur in joueurs:
                if(isinstance(joueur, str)):
                    count += 10
                else:
                    count += joueur['murs']
            count += len(murs['horizontaux'])
            count += len(murs['verticaux'])
        if(count != 20):
            raise QuoridorError

        # si la position d'un mur est invalide.
        if(murs != None):
            for mh in murs['horizontaux']:
                if not (mh[0] in range(1, 9)):
                    raise QuoridorError
                if not (mh[1] in range(2, 10)):
                    raise QuoridorError
            for mv in murs['verticaux']:
                if not (mh[0] in range(2, 10)):
                    raise QuoridorError
                if not (mh[1] in range(1, 9)):
                    raise QuoridorError

        partie = {}
        partie_joueurs = []
        # initialisation des joueurs
        for indice, joueur in enumerate(joueurs):
            if(isinstance(joueur, str)):
                if(indice == 0):
                    j = {'nom': joueur, 'murs': 10, 'pos': [5, 1]}
                else:
                    j = {'nom': joueur, 'murs': 10, 'pos': [5, 9]}
            else:
                j = {'nom': joueur['nom'],
                     'murs': joueur['murs'], 'pos': joueur['pos']}
            partie_joueurs.append(j)

        # initialisation des murs
        mur_horizontaux = mur_verticaux = []
        if(murs != None):
            mur_horizontaux = murs['horizontaux']
            mur_verticaux = murs['verticaux']

        partie['état'] = {'joueurs': partie_joueurs,
                          'murs': {'horizontaux': mur_horizontaux, 'verticaux': mur_verticaux}}
        self.partie = partie

    def __str__(self):
        """ Affiche la matrice sous forme de damier à l'écran """
        # creation d'une matrice vide
        ligne = 21
        colone = 39
        numerotation = 9
        matrice = []
        matrice.append(['Légende: 1=idul, 2=automate'])
        matrice.append(['   -----------------------------------'])
        for i in range(2, ligne-2):
            matrice.append([' ']*colone)
        matrice.append(['--|-----------------------------------'])
        matrice.append(['  | 1   2   3   4   5   6   7   8   9'])
        for i in range(2, ligne-2):
            matrice[i][2] = '|'
            matrice[i][38] = '|'
            if (i % 2) == 0:
                matrice[i][0] = str(numerotation)
                numerotation -= 1
                for j in range(1, 10):
                    matrice[i][4*j] = '.'
        # déchiffrage du json
        j1 = self.partie['état']["joueurs"][0]["pos"]
        j2 = self.partie['état']["joueurs"][1]["pos"]
        mh = self.partie['état']["murs"]["horizontaux"]
        mv = self.partie['état']["murs"]["verticaux"]
        # incorporation des élements du jeu : joueurs et murs
        # convertit les coordonnées des joueurs
        for i in [j1, j2]:
            i[0], i[1] = 2*(10-i[1]), i[0]*4
            # convertit les coordonnées des murs horizontaux
        for i in mh:
            i[0], i[1] = 2*(10-i[1])+1, 4*i[0]-1
            # convertit les coordonnées des murs verticaux
        for i in mv:
            i[0], i[1] = 2*(10-i[1])-2, 4*i[0]-2
            # insère les murs horizontaux
        for i in mh:
            for j in range(i[1], i[1]+7):
                matrice[i[0]][j] = '-'
            # insère les murs verticaux
        for i in mv:
            for j in range(i[0], i[0]+3):
                matrice[j][i[1]] = '|'
            # insère les joueurs
        matrice[j1[0]][j1[1]] = '1'
        matrice[j2[0]][j2[1]] = '2'
        # convertit la matrice en chaine
        for indice, mat1 in enumerate(matrice):
            matrice[indice] = ''.join(mat1)
        return '\n'.join(matrice)


def déplacer_jeton(self, joueur, position):
    position = list(position)
    # si le numéro du joueur est autre que 1 ou 2
    if not(joueur in [1, 2]):
        raise QuoridorError

    # si la position est invalide(en dehors du damier)
    for coord_pos in position:
        if not (coord_pos in range(1, 10)):
            raise QuoridorError

    # si la position est invalide pour l'état actuel du jeu
    for i in [0, 1]:
        [a, b] = self.partie['état']['joueurs'][i]['pos']
        possibilité = [[a, b-1], [a, b+1], [a-1, b], [a+1, b]]
        if b == 1:
            del possibilité[0]
        elif b == 9:
            del possibilité[1]
        if a == 1:
            del possibilité[2]
        elif a == 9:
            del possibilité[3]

        # si la position n'est pas acceptable
        if not(position in possibilité):
            raise QuoridorError

        # s'il y'a un mur horizontal ou vertical
        empechement_mh = [[a, b], [a-1, b], [a, b+1], [a-1, b+1]]
        empechement_mv = [[a, b], [a, b-1], [a+1, b], [a+1, b-1]]
        # bloqué en bas
        if position == [a, b-1]:
            for mh in self.partie['état']['murs']["horizontaux"]:
                if mh in empechement_mh[:2]:
                    raise QuoridorError
            # bloqué en haut
        elif position == [a, b+1]:
            for mh in self.partie['état']['murs']["horizontaux"]:
                if mh in empechement_mh[2:]:
                    raise QuoridorError
            # bloqué à gauche
        if position == [a-1, b]:
            for mh in self.partie['état']['murs']["verticaux"]:
                if mh in empechement_mv[:2]:
                    raise QuoridorError
            # bloqué à droite
        elif position == [a+1, b]:
            for mh in self.partie['état']['murs']["verticaux"]:
                if mh in empechement_mh[:2]:
                    raise QuoridorError
