from turtle import *
from dicoJeu import *
import winsound
import Affichage

def next_cell(dico, direction, sens):
    """
    Retourne les coordonnees de la prochaine cellule en fonction de la direction (vertical, horizontal)
    et du sens (haut -> +, bas -> -, gauche -> -, droite -> +)
    """
    if direction == "up_down":
        x_suivant = xcor()
        y_suivant = ycor() + dico["cote"]  * sens
    else:
        x_suivant = xcor()+ dico["cote"]  * sens
        y_suivant = ycor() 
    cell = Affichage.pixel2cell(x_suivant, y_suivant, dico)
    return cell

def deplacable(dico, direction, sens):
    """
    Verifie que la tortue puisse se deplacer sur le cellule demandee
    """
    cell = next_cell(dico, direction, sens)
    color = "black"
    #Verifie que la cellule demandee est dans le labyrinthe
    if not (0 <= cell[0] <= dico["lignes"]-1 and 0 <= cell[1] <= dico["colonnes"]-1):
        print("cette case est en dehors du labyrinthe...")
        return False, "red"  
    #Si ce n'est pas un mur on verifie quel est le type de la cellule
    if Affichage.typeCellule(cell[0], cell[1]) in ["passage", "sortie", "carrefour", "impasse", "entree"]:
        if Affichage.typeCellule(cell[0], cell[1]) == "carrefour":
            color = "blue"
        elif Affichage.typeCellule(cell[0], cell[1]) == "impasse":
            color = "orange"
        elif Affichage.typeCellule(cell[0], cell[1]) == "sortie":
            color = "green"  
        return True, color 
    #Sinon c'est un mur 
    color = "red"
    print("Vous ne pouvez pas vous deplacer sur cette case", Affichage.typeCellule(cell[0], cell[1]))
    return False, color  

def check_victoire(dico):
    "Permet de Verifier si le joueur a gagne"
    if color() == ('green', 'green'):
        Affichage.Victoire(dico)

def gauche(dico, type = "auto"):
    """Si la tortue peux se deplacer vers la gauche: elle se deplace vers la gauche et ajoute
    son deplacement dans la liste des deplacements"""

    # si la tortue est en mode "manuel" mais que le joueur n'a pas le droite de deplacer la tortue, la fonction s'arrete
    if type == "manuel":
        if dico["can_press_keys"] == False:
            return
    move, clr = deplacable(dico, "", -1)
    if move == True:
        setheading(180)
        forward(dico["cote"])
        winsound.PlaySound("move.wav", winsound.SND_ASYNC)
        dico["commandes"].append("g")
    color(clr)
    check_victoire(dico)

def droite(dico, type = "auto"):
    """Si la tortue peux se deplacer vers la droite: elle se deplace vers la droite et ajoute
    son deplacement dans la liste des deplacements"""

    # si la tortue est en mode "manuel" mais que le joueur n'a pas le droite de deplacer la tortue, la fonction s'arrete
    if type == "manuel":
        if dico["can_press_keys"] == False:
            return

    move, clr = deplacable(dico, "", 1)
    if move == True:
        setheading(0)
        forward(dico["cote"])
        winsound.PlaySound("move.wav", winsound.SND_ASYNC)
        dico["commandes"].append("d")
    color(clr)
    check_victoire(dico)

def bas(dico, type = "auto"):
    """Si la tortue peux se deplacer vers le bas: elle se deplace vers le bas et ajoute
    son deplacement dans la liste des deplacements"""

    # si la tortue est en mode "manuel" mais que le joueur n'a pas le droite de deplacer la tortue, la fonction s'arrete
    if type == "manuel":
        if dico["can_press_keys"] == False:
            return
    
    move, clr = deplacable(dico, "up_down", -1)
    if move == True:
        setheading(-90)
        forward(dico["cote"])
        winsound.PlaySound("move.wav", winsound.SND_ASYNC)
        dico["commandes"].append("b")
    color(clr)
    check_victoire(dico)

def haut(dico, type = "auto"):
    """Si la tortue peux se deplacer vers le haut: elle se deplace vers le haut et ajoute
    son deplacement dans la liste des deplacements"""

    # si la tortue est en mode "manuel" mais que le joueur n'a pas le droite de deplacer la tortue, la fonction s'arrete
    if type == "manuel":
        if dico["can_press_keys"] == False:
            return
    move, clr = deplacable(dico, "up_down", 1)
    if move == True:
        setheading(90)
        forward(dico["cote"])
        winsound.PlaySound("move.wav", winsound.SND_ASYNC)
        dico["commandes"].append("h")
    color(clr)
    check_victoire(dico)

def suivreChemin(li, dico):
    """
    Fait déplacer la tortue selon le chemin entre en parametres
    si le chemin fonctionne, un message de Succes est affiche
    sinon, un message d'erreur est affiche
    """
    possible = True
    for commd in li:
        if commd == "g":
            possible = gauche(dico)
        elif commd == "d":
            possible = droite(dico)
        elif commd == "b":
            possible = bas(dico)
        elif commd == "h":
            possible = haut(dico) 
        if possible == False:
            break
    if possible == False: 
        print("Le chemin demandé est impossible")
    else:
        print("Succes")      

def inverserChemin(li, dico):
    """
    Fait parcourir a la tortue le chemin entre en parametre dans le sens inverse
    """
    newLi = []
    for i in li:
        if i == "g":
            newLi.append("d")
        elif i == "d":
            newLi.append("g")
        elif i == "h":
            newLi.append("b")
        elif i == "b":
           newLi.append("h")
    newLi = newLi[::-1]#inverse la liste
    suivreChemin(newLi, dico)

def direction_origine(dernier_deplacement, case_actuelle):
    """
    Renvoie la cellule par laquelle vient la tortue
    cette fonction est utile pour les carrefours
    """
    case_origine = []
    if dernier_deplacement == "g":
        case_origine.append(case_actuelle[0]+1)
        case_origine.append(case_actuelle[1])
    elif dernier_deplacement == "d":
        case_origine.append(case_actuelle[0]-1)
        case_origine.append(case_actuelle[1])
    elif dernier_deplacement == "h":
        case_origine.append(case_actuelle[0])
        case_origine.append(case_actuelle[1]-1)
    elif dernier_deplacement == "b":
        case_origine.append(case_actuelle[0])
        case_origine.append(case_actuelle[1]+1)
    return case_origine
    

def explorer(dico, case_actuelle, liste_positions = [], l_jonctions = [1], liste_carrefours = []):
    """
    La fonction fait en sorte que la tortue explore automatiquement toutes les voies possibles jusqu'a trouver la sortie
    elle renvoie ensuite le chemin le plus court
    """
    liste_positions.append(case_actuelle) #on ajoute la position actuelle a la liste des cases explorees
    for chemin in l_jonctions:# Pour tous les chemins disponibles
        liste_deplacements = []
        while Affichage.typeCellule(case_actuelle[0], case_actuelle[1]) != "impasse":

            if Affichage.typeCellule(case_actuelle[0], case_actuelle[1]) == "sortie":
                print("Victoire !") 
                return liste_deplacements#on retourne le plus cours chemin

            # Si on arrive a un carrefour, la fonction s'appelle elle meme pour explorer les nouveaux chemins
            if Affichage.typeCellule(case_actuelle[0], case_actuelle[1]) == "carrefour" and case_actuelle not in liste_carrefours:
               liste_carrefours.append(case_actuelle) #on ajoute le carrefour a la liste des carrefours deja visites
               liste_jonctions = Affichage.jonctions(case_actuelle[0], case_actuelle[1])
               liste_jonctions.remove(direction_origine(liste_deplacements[-1], case_actuelle))#parmi les jonctions du carrefour on enleve la cellule d'où on vient              
               liste_positions.remove(case_actuelle)#on enleve la position actuelle car elle sera ajoutee lors de l'appel de la fonction(ligne juste en dessous)
               explorer(dico, case_actuelle, liste_positions, liste_jonctions, liste_carrefours)#on explore la jonction
                    
            # la tortue se deplace si la cellule demandee n'a pas ete exploree et si il est possible de s'y deplacer
            if deplacable(dico, "", -1)[0] == True and ([case_actuelle[0], case_actuelle[1]-1] not in liste_positions):
                gauche(dico)
                case_actuelle = [case_actuelle[0], case_actuelle[1]-1]#on met a jour la case actuelle
                liste_positions.append(case_actuelle)#on ajoute la case actuelle aux cases deja visitees
                liste_deplacements.append("g")#on ajoute le deplacement effectue a la liste des deplacements
            elif deplacable(dico, "", 1)[0] == True and ([case_actuelle[0], case_actuelle[1]+1] not in liste_positions):
                droite(dico)
                case_actuelle = [case_actuelle[0], case_actuelle[1]+1]#on met a jour la case actuelle
                liste_positions.append(case_actuelle)#on ajoute la case actuelle aux cases deja visitees
                liste_deplacements.append("d")#on ajoute le deplacement effectue a la liste des deplacements
            elif deplacable(dico,"up_down", 1)[0] == True and ([case_actuelle[0]-1, case_actuelle[1]] not in liste_positions):
                haut(dico)
                case_actuelle = [case_actuelle[0] -1, case_actuelle[1]]#on met a jour la case actuelle
                liste_positions.append(case_actuelle)#on ajoute la case actuelle aux cases deja visitees
                liste_deplacements.append("h")#on ajoute le deplacement effectue a la liste des deplacements
            elif deplacable(dico,"up_down", -1)[0] == True and ([case_actuelle[0] +1, case_actuelle[1]] not in liste_positions):
                bas(dico)
                case_actuelle = [case_actuelle[0] +1, case_actuelle[1]]#on met a jour la case actuelle
                liste_positions.append(case_actuelle)#on ajoute la case actuelle aux cases deja visitees
                liste_deplacements.append("b")#on ajoute le deplacement effectue a la liste des deplacements
        inverserChemin(liste_deplacements, dico)#On retourne sur la case d'origine  

