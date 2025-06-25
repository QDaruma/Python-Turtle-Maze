from turtle import *
import navigation
import Affichage
import winsound

def load(dico):
    """
    Permet d'Afficher le menu principal et de remettre a 0 les parametres important
    """

    dico["Screen"].reset()#Efface tous les traces de la tortue et la repositionne en (0,0)
    dico["commandes"] = []
    dico["can_press_keys"] = False
    dico["buttons"] = {}
    draw_menu(dico["Screen"], dico)
    winsound.PlaySound("mainsound.wav", winsound.SND_ASYNC + winsound.SND_LOOP)

def draw_menu(window,  dico):
    """
    Dessine le menu principal 
    """
    window.tracer(0)
    window.setup(width=1.0, height=1.0)
    window.bgpic("bg.gif")

    Affichage.positionner(0, 0)
    Affichage.stamp_image("mainmenu.gif")

    #Cree deux boutons (mode automatique/mode manuel) et les ajoute au dictionnaire
    dico["buttons"]["manuelle"] = draw_Button("Manuelle", "#e8ab18" , 300, 150, (-150, -250))
    dico["buttons"]["automatique"] = draw_Button("Automatique", "#7d812c" ,300, 150, (-500, -250))
    dico["buttons"]["quit"] = draw_Button("Quitter", "#de6f20" , 300, 150, (200, -250))
    tracer(1)


def draw_Button(bt_name, color, largeur, hauteur, pos = (0, 0)):
    """
    Dessine un bouton en fonction de la couleur, de la position et des dimensions données en paramètres
    """
    button_coords = []
    button_coords.append(pos)
    button_coords.append((pos[0] + largeur, pos[1] - hauteur))
    Affichage.positionner(pos[0], pos[1])
    
    #Dessine le bouton
    width(5)
    fillcolor(color)
    begin_fill()
    for i in range(2):
        forward(largeur)
        right(90)
        forward(hauteur)
        right(90)
    width(1)
    end_fill()

    #Ecrit le nom du bouton au centre de ce dernier
    Affichage.positionner(pos[0] + largeur/2, pos[1] - hauteur/2)
    write(bt_name, align="center", font=("Arial", 25, "bold"))
    ht() #rend la tortue invisible
    return button_coords

def click_Button(x, y, dico, window):
    """
    Permet de verifier si le joueur a clique sur un boutton
    si oui, la fonction effectue une action differente selon le bouton sur lequel on a clique
    """
    laby = dico["labyrinthe"]
    entree = dico["entree"]
    sortie = dico["sortie"]
    cote = dico["cote"]
    pos = dico["position"]
    buttons = dico["buttons"]
    if len(dico["buttons"]) > 0:
        for button in buttons:
            if buttons[button][0][0] <= x <= buttons[button][1][0] and buttons[button][1][1] <= y <= buttons[button][0][1]:     
                winsound.PlaySound(None, 0)#coupe la musique
                window.tracer(0)
                window.reset()
                #Affiche le labyrinte et positionne la tortue a l'entree
                Affichage.afficheGraphique(laby, entree, sortie, cote, pos[0], pos[1])
                up()
                goto(Affichage.cell2pixel(entree[0], entree[1], cote, pos[0], pos[1])) 
                color("black")            
                showturtle()
                window.tracer(1)

                if button == "automatique": 
                    #on supprime les cles manuelles et automatique pour eviter que le joueur ne puisse cliquer pendant l'exploration
                    dico["buttons"] = {}
                    navigation.explorer(dico, dico["entree"], [], [1], [])
                if button == "manuelle":
                    #on supprime les cles manuelles et automatique pour eviter que le joueur ne puisse cliquer pendant l'exploration
                    dico["buttons"] = {}
                    dico["can_press_keys"] = True
                elif button == "quit":
                    quit()
                break
                
        
                
                
            