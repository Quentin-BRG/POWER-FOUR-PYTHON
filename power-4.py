#----------------------------------------------------------#
#------------ PUISSANCE 4 ---------------------------------#
#------------ DEV BY : JOSHUA -----------------------------#
#------------ -------- ADRIEN -----------------------------#
#------------ -------- LENY -------------------------------#
#------------ -------- QUENTIN ----------------------------#
#----------------------------------------------------------#

# Importer le module pour mettre le texte en couleur
from colorama import init, Fore
import random
import time
# Remettre la couleur en mode normal (blanc) à chaque fin de print()
init(autoreset=True)
mode = 0
#-------------------------------------------------------------------#
#------------ EXERCICE 1 -------------------------------------------#
#- DESCR : renvoie une grille de dimension l*c vide (remplie de 0) -#
#-------------------------------------------------------------------#


def grille_vide():
    global mode
    l = min(max(
        int(input(Fore.WHITE + "Entrez le nombre de ligne : " + Fore.GREEN + "")), 1), 60)
    c = min(max(int(
        input(Fore.WHITE + "Entrez le nombre de colonne : " + Fore.GREEN + "")), 1), 70)
    mode = int(
        input(Fore.WHITE + "Entrez le mode de jeu (1/2/3) : " + Fore.GREEN + ""))
    # Créer la grille avec une liste de listes par comprehension
    g = [[0]*c for i in range(l)]
    return g

#----------------------------------------------------------#
#------------ EXERCICE 2 ----------------------------------#
#- DESCR : afficher la grille du jeu ----------------------#
#----------------------------------------------------------#


def afficher(g):
    print("""###################################################""")
    left_space = " "*7  # Définir la distance entre l'index des lignes et le tableau
    print(left_space, end="")  # Afficher cette distance
    for index in range(len(g[0])):  # Pour chaque colonne, afficher l'index
        print("<", index, ">", end="")
    print("\n")
    for ligne in range(len(g)):  # Regarder dans chaque ligne
        # Afficher l'index de la ligne
        print("<", (len(g)-1)-ligne, ">", end=" ")
        # Definir et afficher la distance entre l'index des lignes et le tableau
        print(left_space[0:len(left_space)-(5+1)], end="")
        for case in g[ligne]:  # Regarder dans chaque case
            if case == 0:
                symbole = " "
            elif case == 1:
                symbole = Fore.RED + "●"
            elif case == 2:
                symbole = Fore.YELLOW + "●"
            print(Fore.BLACK + "|", symbole, Fore.BLACK +
                  "|", end="")  # Aficher la valeur de la case
        print("\n", end="")  # Revenir à la ligne au niveau de chaque ligne
        # Définir et afficher la distance entre l'index des lignes et le tableau
        print(left_space, end="")
        # Afficher une droite qui sépare les lignes
        print(Fore.BLACK + "-"*5*len(g[0]))
    print()  # Revenir à la ligne

#-------------------------------------------------------------------------------------#
#------------ EXERCICE 3 -------------------------------------------------------------#
#- DESCR : renvoie un booleen indiquant s'il est possible de jouer dans la colonne c -#
#-------------------------------------------------------------------------------------#


def coup_possible(c, g):
    # Verifier si le joueur a bien rentrer une valeur
    if c == None or c > len(g[0])-1 or c < 0:
        return False
    if g[0][c] == 0:  # Verifier que la case est bien vide
        return True
    else:
        return False

#----------------------------------------------------------#
#------------ EXERCICE 4 ----------------------------------#
#- DESCR : place le jeton du joueur j dans la colonne c  --#
#----------------------------------------------------------#


def jouer(g, j, c):
    # Définir par défaut la derniere ligne (au cas ou la colonne serait vide)
    a = len(g)-1
    for ligne in range(len(g)):  # regarder dans chacunes des lignes
        if g[ligne][c] != 0:  # verifier que la case est vide ou non
            a = ligne-1  # Attribut la valeur de ligne precedente
            break  # Arreter la boucle : nous sommes en bas de la colonne
    g[a][c] = j  # Affecter la valeur de la case a la valeur du joueur
    return a, c


#----------------------------------------------------------#
#------------ EXERCICE 5 ----------------------------------#
#- DESCR : programme principal v1  ----------------------- #
#----------------------------------------------------------#
"""
grid = grille_vide() #creer une grille
joueur = 1 #c'est le joueur 1 qui commence

while True: #boucle infini (condition toujours vrai)
    afficher(grid)
    choice = None #le joueur n'a toujours pas choisi une case
        if (joueur == 1) or (joueur == 2 and mode == 1):
            # demander au joueur de choisir une case
            sentence = Fore.RED + "Joueur " + \
                str(joueur) + Fore.WHITE + " , selectionnez une colonne : "
            choice = int(input(Fore.WHITE + sentence + Fore.GREEN + ""))
        elif mode == 2:
            choice = random.randint(0,len(grid))
    jouer(grid, joueur, choice) #changer de joueur
    if joueur == 1:
        joueur = 2
    else:
        joueur = 1
"""
#----------------------------------------------------------#
#------------ EXERCICE 6 ----------------------------------#
#----------------------------------------------------------#


def partie_nulle(g):
    prod = 1
    for case in g[0]:
        prod = prod*case  # Faire le produit de la première ligne
    if prod == 0:  # Vérifier si elle est égale à 0
        return False
    else:
        return True

#----------------------------------------------------------#
#------------ EXERCICE 7 ----------------------------------#
#----------------------------------------------------------#


def horiz(g, j, l, c):
    aux = 0
    for coef in [1, -1]:  # Dans un sens puis dans l'autre
        for i in range(1, 4, 1):  # Vérifier 3 fois (pour avoir une ligne de 4 (3+1))
            # Vérifier si la ligne se trouve dans la grille
            if c+i*coef <= len(g[0])-1 and c+i*coef >= 0:
                if g[l][c+i*coef] == j:  # Vérifier si la case est égale au joueur
                    aux = aux + 1
                else:
                    break  # Arreter la boucle
    if aux >= 3:
        return True
    else:
        return False

#----------------------------------------------------------#
#------------ EXERCICE 8 ----------------------------------#
#----------------------------------------------------------#


def vert(g, j, l, c):
    aux = 0
    for coef in [1, -1]:  # Dans un sens puis dans l'autre
        for i in range(1, 4, 1):  # Vérifier 3 fois (pour avoir une ligne de 4 (3+1)
            # Vérifier si la ligne se trouve dans la grille
            if l+i*coef <= len(g)-1 and l+i*coef >= 0:
                if g[l+i*coef][c] == j:  # Vérifier si la case est égale au joueur
                    aux = aux + 1
                else:
                    break  # Arreter la boucle
    if aux >= 3:
        return True
    else:
        return False
#----------------------------------------------------------#
#------------ EXERCICE 9 ----------------------------------#
#----------------------------------------------------------#


def diagonale_SO_NE(g, j, l, c):
    aux = 0
    for coef in [1, -1]:  # Dans un sens puis dans l'autre
        for i in range(1, 4, 1):  # Vérifier 3 fois (pour avoir une ligne de 4 (3+1)
            # Vérifier si la ligne se trouve dans la grille
            if l+i*coef <= len(g)-1 and l+i*coef >= 0 and c+i*coef <= len(g[0])-1 and c+i*coef >= 0:
                if g[l+i*coef][c+i*coef] == j:  # Vérifier si la case est égale au joueur
                    aux = aux + 1
                else:
                    break  # Arreter la boucle
    if aux >= 3:
        return True
    else:
        return False

#----------------------------------------------------------#
#------------ EXERCICE 10 ---------------------------------#
#----------------------------------------------------------#


def diagonale_SE_NO(g, j, l, c):
    aux = 0
    for coef in [1, -1]:  # Dans un sens puis dans l'autre
        for i in range(1, 4, 1):  # Vérifier 3 fois (pour avoir une ligne de 4 (3+1)
            # Vérifier si la ligne se trouve dans la grille
            if l+i*coef <= len(g)-1 and l+i*coef >= 0 and c-i*coef <= len(g[0])-1 and c-i*coef >= 0:
                if g[l+i*coef][c-i*coef] == j:  # Vérifier si la case est égale au joueur
                    aux = aux + 1
                else:
                    break  # Arreter la boucle
    if aux >= 3:
        return True
    else:
        return False
#----------------------------------------------------------#
#------------ EXERCICE 11 ---------------------------------#
#----------------------------------------------------------#


def vict(g, j, l, c):
    if vert(g, j, l, c) or horiz(g, j, l, c) or diagonale_SE_NO(g, j, l, c) or diagonale_SO_NE(g, j, l, c):
        return True
    else:
        return False


#----------------------------------------------------------#
#------------ EXERCICE 12 ---------------------------------#
#----------------------------------------------------------#
print(Fore.BLUE + "#######################################\n#            " + Fore.WHITE +
      "PUISSANCE 4"+Fore.BLUE+"              #\n#######################################")
grid = grille_vide()  # creer une grille
joueur = 2  # c'est le joueur 1 qui commence puisque on change de joueur à chaque

l = 0
c = 0

# boucle infini (condition toujours vrai)
# tant que personne n'a gagné ET que ce n'est pas une partie nulle
while not (vict(grid, joueur, l, c)) and not (partie_nulle(grid)):
    # changer de joueur
    if joueur == 1:
        joueur = 2
    else:
        joueur = 1
    if mode != 3:
        afficher(grid)

    choice = None  # le joueur n'a toujours pas choisi une case
    while not (coup_possible(choice, grid)):  # tant que le joueur n'a pas choisi une case
        if (joueur == 1 and (mode == 1 or mode == 2)) or (joueur == 2 and mode == 1):
            # demander au joueur de choisir une case
            sentence = Fore.RED + "Joueur " + \
                str(joueur) + Fore.WHITE + " , selectionnez une colonne : "
            choice = int(input(Fore.WHITE + sentence + Fore.GREEN + ""))
        elif mode == 2 or mode == 3:
            choice = random.randint(0, len(grid))
    l, c = jouer(grid, joueur, choice)

if partie_nulle(grid):
    afficher(grid)
    print("Partie nulle !")
else:  # Si il y a une victoire ou une partie nulle mais que ce n'est pas une partie nulle, c'est une victoire
    afficher(grid)
    print(Fore.BLUE + "#######################################\n#        " + Fore.RED + "Joueur " +
          str(joueur) + Fore.WHITE + " a gagné(e) !        "+Fore.BLUE+"#\n#######################################")
time.sleep(4)  # temps d'attente afin de fermer le programme
