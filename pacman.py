########## Importer les modules necessaires ##############
from tkinter import *
from random import *
import time
from tkinter.font import Font
##########################################################
##########    Fonctions ##################################
##########################################################
def affichage():
    global donnees_cases
    x = 480 #coordonnées x de la case
    y = 135 #coordonnées y de la case
    for ligne in range(16): #ligne
        for e in donnees_cases[ligne]:  #[ligne] = sous-liste dans laquelle on parcours par élément
            if e==0:
                pass #rien
            elif e==1:
                Canevas.create_oval(x-5,y-5,x+5,y+5,fill='#FFC482') #pièce
            elif e==2:
                Canevas.create_oval(x-20,y-20,x+20,y+20,fill='red') #étoile
            elif e==3:
                Canevas.create_rectangle(x-25,y-25,x+25,y+25,fill='blue') #mur
            x+=50
        x=480
        y+=50

def coordonnees_depart(): #coordonnees de départ du joueur et des ennemis. Cette fonction peut aussi être appelée lors d'un game over.
    global coos_joueur, coos_ennemis
    Canevas.create_oval(coos_joueur[0],coos_joueur[1],fill='yellow') #joueur
    Canevas.create_polygon(coos_ennemis[0][0],coos_ennemis[0][1],coos_ennemis[0][2],fill='brown') #ennemi 1
    Canevas.create_polygon(coos_ennemis[1][0],coos_ennemis[1][1],coos_ennemis[1][2],fill='brown') #ennemi 2
    Canevas.create_polygon(coos_ennemis[2][0],coos_ennemis[2][1],coos_ennemis[2][2],fill='brown') #ennemi 3
    Canevas.create_polygon(coos_ennemis[3][0],coos_ennemis[3][1],coos_ennemis[3][2],fill='brown') #ennemi 4
##########################################################
##########    Variables ##################################
##########################################################
#0=rien  1=pièce  2=étoile  3=mur                         20 colonnes
donnees_cases=[[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3], #ligne 0 (bordure haut)
               [3,1,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,3], #ligne 1
               [3,1,1,1,1,1,1,1,1,3,3,1,1,1,1,1,1,1,1,3], #ligne 2
               [3,1,1,3,3,3,3,1,1,3,3,1,1,3,3,3,3,1,1,3], #ligne 3
               [3,1,1,3,0,0,3,1,1,3,3,1,1,3,0,0,3,1,1,3], #ligne 4
               [3,1,1,3,0,0,3,1,1,3,3,1,1,3,0,0,3,1,1,3], #ligne 5
               [3,1,1,3,3,3,3,1,1,3,3,1,1,3,3,3,3,1,1,3], #ligne 6
               [3,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,3], #ligne 7
               [3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3], #ligne 8
               [3,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,3], #ligne 9
               [3,0,0,3,0,0,3,3,3,3,3,3,3,3,0,0,3,0,0,3], #ligne 10
               [3,0,0,3,0,0,3,2,0,3,3,0,2,3,0,0,3,0,0,3], #ligne 11
               [3,0,0,3,3,3,3,0,0,3,3,0,0,3,3,3,3,0,0,3], #ligne 12
               [3,0,0,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,3], #ligne 13
               [3,0,0,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,3], #ligne 14
               [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]] #ligne 15 (bordure bas)

coos_joueur=[[955,460],[1005,510]] 

#points : haut, bas-gauche, bas-droite
coos_ennemis=[[[530,165],[510,205],[550,205]],      #haut-gauche
              [[1380,165],[1360,205],[1400,205]],   #haut-droite
              [[530,815],[510,855],[550,855]],      #bas-gauche
              [[1380,815],[1360,855],[1400,855]]]   #bas-droite
              
#########################################################
########## Interface graphique ##########################
##########################################################
Mafenetre = Tk()
Mafenetre.title("Titre")
Canevas = Canvas(Mafenetre,width=1920,height=1080,bg ='black')
Mafenetre.attributes("-fullscreen", True)
Canevas.pack()
font = Font(family='Arial', size=200)
###########################################################
########### Receptionnaire d'évènement ####################
###########################################################

##########################################################
############# Programme principal ########################
##########################################################
affichage()
coordonnees_depart()
###################### FIN ###############################
Mafenetre.mainloop()
