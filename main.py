#1.
"""

(3,1)
-1
1
-1
1

"""

#2.

"""

bouger("S")
bouger("O")
bouger("N")
bouger("N")
bouger("N")
bouger("E")
bouger("E")

"""

#3.
global grille
grille = [[0,0,1,0],[0,0,0,0],[2,0,0,4],[0,-1,0,0],[0,3,0,0]]
global nbLignes,nbColonnes
nbLignes = len(grille)
nbColonnes = len(grille[0])
global robotsSauves
robotsSauves = []

def bouger():
    for ligne in range(nbLignes):
        for colonne in range(nbColonnes):
            contenuCase = grille[ligne][colonne]
        if contenuCase > 0:
            grille[ligne][colonne] = 0
        if colonne > 0:
            if grille[ligne][colonne - 1] == -1:
                robotsSauves.append(contenuCase)
        else:
            grille[ligne][colonne - 1] = contenuCase

def afficherEtat(x):
    if x not in robotsSauves:
        for ligne in range(nbLignes):
            for colonne in range(nbColonnes):
                contenuCase = grille[ligne][colonne]
                if contenuCase == x:
                    return (ligne, colonne)
        return -1
    return 1
for i in range(4) :
    print(afficherEtat(i+1))

#cout quadratique, nblignes*nbcolonnes

#B.

#4
"""
On peut implémenter une liste contenant les mouvement des robots, a partir de leur position initiale pour aller jusqu'au drapeau. De plus on fera une variable
mouvement qui nous donnera les mouvement effectués par les robots (x,y) , ainsi quand on bouge vers le nord: x+=1

"""

#5.
#a. b. c.
"""
On va créer une variable globale mouvement. Cette variable contiendra les mouvements des robots. 
de plus on va garder la liste avec les coordonées des robots dedans. on va stocker les coordonées des robots ainsi que xdeplacementmax et ydeplacement max
De plus on va regarder a chaque deplacement a la case des coordonnees du drapeau + le déplacement si il y a un robot dedans.
Si oui alors on vérifie s'il est sorti auparavant de la grille grace a xmax et ymax 
Si non le mettre comme gagner, lors de afficher etat, si il n'est pas dans la liste des gagner alors verifier s'il est sorti grace a xmax et ymax.
Sinon mettre ses coordonées avec l'addition de x et y actuels des deplacements.

"""


global mouvement
mouvement = [0,0]
global xmax_haut,ymax_droite,xmax_bas,ymax_gauche
xmax_haut = 0
ymax_droite = 0
xmax_bas = 0
ymax_gauche = 0

global position_initiale
position_initiale = dict()
for ligne in range(nbLignes):
    for colonne in range(nbColonnes):
        contenuCase = grille[ligne][colonne]
        if contenuCase >=1:
            position_initiale[contenuCase] = (ligne,colonne)


global coord_flag
for i in range(len(grille)):
    for j in range(len(grille[i])):
        if grille[i][j] == -1:
            coord_flag = (i,j)

def is_out(x):
    if position_initiale[x][0] + xmax_haut > nbLignes or position_initiale[x][0] + xmax_bas < 0 or position_initiale[x][1] + ymax_droite > nbColonnes or position_initiale[x][1] + ymax_gauche <0:
        return True

def bouger_opti(direction,grille1=grille):
    if direction == "N":
        mouvement[0] += 1
    if direction == "S":
        mouvement[0] -= 1
    if direction == "E":
        mouvement[1] += 1
    if direction == "O":
        mouvement[1] -= 1

    if mouvement[0] > xmax_haut:
        xmax_haut = mouvement[0]
    if mouvement[0] < xmax_bas:
        xmax_bas = mouvement[0]
    if mouvement[1] > ymax_droite:
        ymax_droite = mouvement[1]
    if mouvement[1] < ymax_gauche:
        ymax_gauche = mouvement[1]

    try:
        point = grille1[coord_flag[0] + mouvement[0],coord_flag[1] + mouvement[1]]
        if point >=1:
            if not is_out(point):
                if grille1[point] not in robotsSauves:
                    robotsSauves.append(point)
    except:
        pass


def afficherEtat_opti(x):
    if x in robotsSauves:
        return 1
    elif is_out(x):
        return -1
    else:
        return (position_initiale[x][0] + mouvement[0], position_initiale[x][1] + mouvement[1])


#C. Tous les sous-ensembles sauvables.
#6)

"""

On commence par la donner en binaire, ce qui nous donnera alors pour l'ensemble de robots sauvés 5, 8 et 10: 1010010000
en décimal(base 10) on a donc: 1*2**4 + 1*2**7 + 1*2**9 = 16+128+512 = 656 Le nombre corredpondant à la représentation du sous-ensemble constitué des robots 5, 8 et 10 est donc 656.

"""

#7)

def union(a,b):
    return a | b
#grace à l'opérateur | qui permet de faire l'union de deux nombres.

#8)
#On peut le faire de plusieurs manieres notamment en convertissant en binaire et en regardant la présance d'un 1. Ou sinon on effectue un décalage de bit vers la droite et quand il y a un changement de nombre c'est qu'un  robot est présent.
#On va ici utiliser la fonction bin(x) qui permet de convertir un nombre en binaire. Et on va regarder à quel endroit il y a un bit égal à 1.
def robots_sauves(nombre):
    result = list()
    binaire = bin(nombre)[2:]
    for i in range (1,len(binaire)+1):
        if binaire[-i] == "1":
            result.append(i)
    return result

print(robots_sauves(16))


#9)
import copy
"""

On va d'abord commencer par calculer tous les robots à sauver dans le sous ensemble, pour cela on va utiliser la fonction créée précédemment.
Ensuite on va garder seulement les robots présents dans le sous ensemble ainsi que le drapeau dans la grille initiale.

"""
x = 45 #nombre de robots à sauver, il n'a pas de valeurs prédéfinies.
robotsaSauver = robots_sauves(x)
"""
global grille_sauve
grille_sauve = copy.deepcopy(grille)
for i in range(len(grille_sauve)):
    for j in range(len(grille_sauve[i])):
        if grille_sauve[i][j] not in robotsaSauver and grille_sauve[i][j] !=-1:
            grille_sauve[i][j] = 0

print(robotsaSauver,grille,grille_sauve)
"""
"""

ensuite on va regarder le robot le plus ua nord du drapeau puis celui le plus au sud puis est puis ouest.

"""
global N_max, S_max, E_max, O_max


N_max = 0
S_max = 0
E_max = 0
O_max = 0

def update():
    for i in range(len(robotsaSauver)):
        if position_initiale[robotsaSauver[i]][0]+mouvement[0] > N_max:
            N_max = position_initiale[robotsaSauver[i]][0]+mouvement[0]
        if position_initiale[robotsaSauver[i]][0]+mouvement[0] < S_max:
            S_max = position_initiale[robotsaSauver[i]][0]+mouvement[0]
        if position_initiale[robotsaSauver[i]][1] + mouvement[1] > E_max:
            E_max = position_initiale[robotsaSauver[i]][1]+mouvement[1]
        if position_initiale[robotsaSauver[i]][1] + mouvement[1] < O_max:
            O_max = position_initiale[robotsaSauver[i]][1]+mouvement[1]
    if N_max < coord_flag[0]:
        N_max = None
    else:
        N_max -= coord_flag[0] #il s'agit de sa distance au drapeau
    if S_max > coord_flag[0]:
        S_max = None
    else:
        S_max -= coord_flag[0]
    if E_max < coord_flag[1]:
        E_max = None
    else:
        E_max -= coord_flag[1]
    if O_max > coord_flag[1]:
        O_max = None
    else:
        O_max -= coord_flag[1]

"""

Maintenant on va déplacer tous les robots du plus grand déplacement et on va vérifier si il y en a un qui sort de la grille.

"""

backup_grille = copy.deepcopy(grille)

est_fini = False

while not est_fini:
    if N_max != None:
        for i in range(N_max):
            bouger_opti("N")
        reussite = True
        for i in range(len(robotsaSauver)):
            if afficherEtat_opti(robotsaSauver[i]) == -1:
                reussite = False
                break
        if reussite:
            etats = True
            for i in range(len(robotsaSauver)):
                if afficherEtat_opti(robotsaSauver[i]) == -1:
                    etats = False
                    break
            if etats:
                est_fini = True
                gagne = True
                break
            update()
        else:
            grille = copy.deepcopy(backup_grille)
            if S_max != None:
                for i in range(S_max):
                    bouger_opti("S")
                reussite = True
                for i in range(len(robotsaSauver)):
                    if afficherEtat_opti(robotsaSauver[i]) == -1:
                        reussite = False
                        break
                if reussite:
                    etats = True
                    for i in range(len(robotsaSauver)):
                        if afficherEtat_opti(robotsaSauver[i]) == -1:
                            etats = False
                            break
                    if etats:
                        est_fini = True
                        gagne = True
                        break
                    update()
                else:
                    grille = copy.deepcopy(backup_grille)
                    if E_max != None:
                        for i in range(E_max):
                            bouger_opti("E")
                        reussite = True
                        for i in range(len(robotsaSauver)):
                            if afficherEtat_opti(robotsaSauver[i]) == -1:
                                reussite = False
                                break
                        if reussite:
                            etats = True
                            for i in range(len(robotsaSauver)):
                                if afficherEtat_opti(robotsaSauver[i]) == -1:
                                    etats = False
                                    break
                            if etats:
                                est_fini = True
                                gagne = True
                                break
                            update()
                        else:
                            grille = copy.deepcopy(backup_grille)
                            if O_max != None:
                                for i in range(O_max):
                                    bouger_opti("O")
                                reussite = True
                                for i in range(len(robotsaSauver)):
                                    if afficherEtat_opti(robotsaSauver[i]) == -1:
                                        reussite = False
                                        break
                                if reussite:
                                    etats = True
                                    for i in range(len(robotsaSauver)):
                                        if afficherEtat_opti(robotsaSauver[i]) == -1:
                                            etats = False
                                            break
                                    if etats:
                                        est_fini = True
                                        gagne = True
                                        break
                                    update()
                                else:
                                    est_fini = True
                                    gagne = False


#10)

"""

Si on a le plus grand ensemble de robots sauvables, tous les sous ensembles de celui la le seront aussi.
On commence par regarder si tous les robots sont sauvables, si oui tous les sous ensembles le sont aussi.



"""



