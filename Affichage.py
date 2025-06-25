from turtle import *
import dicoJeu
import Menu
import math
import winsound
import time

def labyFromFile(fn) :
    """
    Lecture d'un labyrinthe dans le fichier de nom fn
    Read a maze from the file named fn.
    """
    f = open(fn)
    laby = []
    indline = 0
    for fileline in f:
        labyline = []
        inditem = 0
        for item in fileline:
            # empty cell / case vide
            if item == ".":
                labyline.append(0)
            # wall / mur
            elif item == "#":
                labyline.append(1)
            # entrance / entree
            elif item == "x":
                labyline.append(0)
                mazeIn = [indline, inditem]
            # exit / sortie
            elif item == "X":
                labyline.append(0)
                mazeOut = [indline, inditem]
            # discard "\n" char at the end of each line
            inditem += 1
        laby.append(labyline)
        indline += 1
    f.close()
    return laby, mazeIn, mazeOut


def afficheTextuel(labyrinthe, entree, sortie):
    """
    affiche le labyrinthe sous forme textuelle (mur:#, passage:" ", entree:x, sortie:o)
    """
    for i in range(len(labyrinthe)):
        for j in range(len(labyrinthe[i])):
            if labyrinthe[i][j] == 1:
                print("#", end = "")
            elif labyrinthe[i][j] == 0:
                if i == entree[0] and j == entree[1]:
                    print("x", end="")
                elif i == sortie[0] and j == sortie[1]:
                    print("o", end="")
                else:
                    print(" ", end = "")
        print("") #retour a la ligne

def carre(cote, color):
    """
    Trace un carre de cote de longueur X et la colorie avec la couleur donnée en parametre
    """
    fillcolor(color)
    begin_fill()
    down()
    for i in range(4):
        forward(cote)
        right(90)
    end_fill()
    up()
    forward(cote)

def positionner(posx, posy):
    """
    Positionne la tortue à l'emplacement demandee
    """
    up()
    setx(posx)
    sety(posy)
    down()

def afficheGraphique(labyrinthe, entree, sortie, cote, posx, posy):
    """
    Trace le labyrinthe graphiquement avec une coordonnee de depart et une largeur donnee
    Toutes cases changent de couleur en fonction de leur nature (mur:gris, passage:blanc, entree:jaune, 
    sortie:vert, carrefour:cyan, impasse:violet) 
    """
    positionner(posx, posy)
    color = ""
    for i in range(len(labyrinthe)):
        for j in range(len(labyrinthe[i])):
            if labyrinthe[i][j] == 1:
                color = "#404040"
            elif labyrinthe[i][j] == 0:
                if i == entree[0] and j == entree[1]:
                    color = "#e7eca3"
                elif i == sortie[0] and j == sortie[1]:
                    color = "#9de19a"
                elif typeCellule(i, j) == "carrefour": 
                        color = "#57F8C8"
                elif typeCellule(i, j) == "impasse": 
                        color = "#bca9e1"
                else:
                    color = "#FFFFFF"     
            carre(cote, color)
        positionner(posx,  ycor() - cote)


def pixel2cell(x,y, dico):
    """
    Prend en parametre des coordonnees de position(x/y) et les converti en coordonnees de cellule (ligne/colonne)
    """
    x -= dico["position"][0]
    y -= dico["position"][1]
    cell = []
    cell.append(math.floor(-y/dico["cote"])) #lignes
    cell.append(math.floor(x/dico["cote"])) #colonnes
    return cell

def testClic(x,y, dico):
    """
    Reçoit les coordonnees d'un click et verifie que ce dernier correspond à une cellule du labyrinthe
    si les coordonnees sont dans le labyrinthe: il affiche la cellule correspondante
    sinon il affiche un message d'erreur 
    """
    index_ligne_max = len(dico["labyrinthe"]) - 1
    index_colonne_max = len(dico["labyrinthe"][index_ligne_max]) - 1
    coordMax = (index_ligne_max, index_colonne_max)   
    coords = pixel2cell(x,y, dico)
    if 0 <= coords[0] <= coordMax[0] and 0 <= coords[1] <= coordMax[1]:
        print(coords)
    else:
        print("Vous n'avez cliqué sur aucune case...")


def cell2pixel(i,j, cote, posx, posy):
    """
    Prend en parametre des coordonnees de cellule (ligne/colonne) et les converti en coordonnees de position(x/y)
    """
    x = math.floor((j+1) * cote) +posx
    y = math.floor(-1 *(i+1) * cote) +posy
    x = x - cote/2
    y = y + cote/2
    return x, y

def jonctions(i, j):
    """
    Compte le nombre de jonctions que possède une case
    """
    liste_jonctions = []
    labyrinthe = dicoJeu.donnees["labyrinthe"]
    if labyrinthe[i-1][j] == 0:
        liste_jonctions.append([i-1,j])
    if labyrinthe[i+1][j] == 0:
        liste_jonctions.append([i+1,j])
    if labyrinthe[i][j-1] == 0:
        liste_jonctions.append([i,j-1])
    if labyrinthe[i][j+1] == 0:
        liste_jonctions.append([i,j+1])
    return liste_jonctions

def typeCellule(i, j): 
    """
    Renvoie le type de la cellule du labyrinthe reçu en parametres
    """

    type_cellule = "mur"
    liste_jonctions = []
    labyrinthe = dicoJeu.donnees["labyrinthe"]
    # Si la cellule n'est pas un mur
    if labyrinthe[i][j] == 0:
        if i == dicoJeu.donnees["entree"][0] and j == dicoJeu.donnees["entree"][1]:
            type_cellule = "entree"
        elif i == dicoJeu.donnees["sortie"][0] and j == dicoJeu.donnees["sortie"][1]:
            type_cellule = "sortie"
        else:
            # On Regarde le nombre de jonctions que possede la case pour savoir si c'est un passage, une impasse ou un carrefour
            liste_jonctions = jonctions(i, j)
            if len(liste_jonctions) >= 3:
                type_cellule = "carrefour"
            elif len(liste_jonctions) == 1:
                type_cellule = "impasse"
            elif 1 <= len(liste_jonctions) <3:
                type_cellule = "passage"
    return type_cellule

def stamp_image(name):
    "Affiche une image a l'ecran"
    addshape(name)
    shape(name)
    stamp()
    shape("turtle")

def Victoire(dico):
    "Affiche le message de victoire puis relance une partie"
    time.sleep(0.5)
    hideturtle()
    winsound.PlaySound("victory.wav", winsound.SND_ASYNC)
    goto(0, 0)
    stamp_image("victory.gif")
    time.sleep(2)
    Menu.load(dico)#permet de relancer la partie