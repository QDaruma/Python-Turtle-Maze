from Affichage import *
from dicoJeu import *
from turtle import *
from navigation import *
from Menu import *

#Initialisation des variables
fileName = "laby1.laby"#input("Entrez le nom d'un fichier contenant la description d'un labyrinthe: ")
labyrinthe, entree, sortie = labyFromFile(fileName)
cote = 60 #largeur des carres formant le labyrinthe
posx, posy = -480, 350 #coordonnees du coin superieur gauche
speed = 10 
colormode(255)

#Stockage de donnees dans le dictionnaire
donnees["labyrinthe"] = labyrinthe
donnees["entree"] = entree
donnees["sortie"] = sortie
donnees["cote"] = cote
donnees["position"] = (posx, posy)
donnees["lignes"] = len(labyrinthe) #nombre de lignes que possede le labyrinthe
donnees["colonnes"] = len(labyrinthe[0]) #nombre de colonnes que possède le labyrinthe

donnees["commandes"] = []
donnees["can_press_keys"] = False #permet de verifier si le joueur peut appuyer sur le clavier
donnees["Screen"] = Screen()

load(donnees) #affiche le menu principal
onscreenclick(lambda x, y: click_Button(x, y, donnees, donnees["Screen"]))#permet de clicker sur les boutons du menu principal
#la tortue se deplace dans la direction demandee (seulement si donnees["can_press_keys"] est egal a True)
onkeypress(lambda: navigation.gauche(donnees, "manuel"), "Left")
onkeypress(lambda: navigation.droite(donnees, "manuel"), "Right")
onkeypress(lambda: navigation.haut(donnees, "manuel"), "Up")
onkeypress(lambda: navigation.bas(donnees, "manuel"), "Down")
listen()
mainloop()


