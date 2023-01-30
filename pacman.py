########## Importer les modules necessaires ##############
from tkinter import *
from random import *
import time
from tkinter.font import Font
##########################################################
##########    Fonctions ##################################
##########################################################
def affichage(): #affichage du terrain de jeu
    global donnees_cases
    x = 480 #coordonnées x de la case (à gauche)
    y = 135 #coordonnées y de la case (en haut)
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

def coordonnees_depart(): #coordonnees de départ du joueur et des ennemis.
    global coos_joueur, coos_ennemis, joueur, ennemi1, ennemi2, ennemi3, ennemi4
    joueur=Canevas.create_oval(coos_joueur[0],coos_joueur[1],fill='yellow')
    ennemi1=Canevas.create_polygon(coos_ennemis[0][0],coos_ennemis[0][1],coos_ennemis[0][2],fill='brown')
    ennemi2=Canevas.create_polygon(coos_ennemis[1][0],coos_ennemis[1][1],coos_ennemis[1][2],fill='brown')
    ennemi3=Canevas.create_polygon(coos_ennemis[2][0],coos_ennemis[2][1],coos_ennemis[2][2],fill='brown')
    ennemi4=Canevas.create_polygon(coos_ennemis[3][0],coos_ennemis[3][1],coos_ennemis[3][2],fill='brown')

def joueur_droite(ev=None): #si touche de droite cliquée
    global direction
    if direction!='droite':
        direction='droite'

def joueur_gauche(ev=None):
    global direction
    if direction!='gauche':
        direction='gauche'

def joueur_haut(ev=None):
    global direction
    if direction!='haut':
        direction='haut'
def joueur_bas(ev=None):
    global direction
    if direction!='bas':
        direction='bas'

def avance():
    [a,b,c,d] = Canevas.coords(joueur)
    i = conversion(a,b)[0] 
    j = conversion(a,b)[1] #coordonnées i,j du joueur
    if direction=='droite':
        if donnees_cases[j][i+1]!=3:
            Canevas.coords(joueur,a+50,b,c+50,d)
            #si  piece : ramasse
            
    if direction=='gauche':
        if donnees_cases[j][i-1]!=3:
            Canevas.coords(joueur,a-50,b,c-50,d)
    if direction=='haut':
        if donnees_cases[j-1][i]!=3:
            Canevas.coords(joueur,a,b-50,c,d-50)
    if direction=='bas':
        if donnees_cases[j+1][i]!=3:
            Canevas.coords(joueur,a,b+50,c,d+50)
    Canevas.update()
    Mafenetre.after(200, avance)

def conversion(x,y): #retourne les coordonées i et j
    convX=1.0
    convY=1.0
    while x>480:
        x-=25
        convX+=0.5
    while y>135:
        y-=25
        convY+=0.5
    if convX<1:
        convX=1
    if convY<1:
        convY=1
    return [int(convX),int(convY)]
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

direction=None
#########################################################
########## Interface graphique ##########################
##########################################################
Mafenetre = Tk()
Mafenetre.title("Titre")
Canevas = Canvas(Mafenetre,width=1920,height=1080,bg ='black')
#Mafenetre.attributes("-fullscreen", True)
Canevas.pack()
Mapolice = Font(family='auto digital', size=100)
Canevas.create_text(200,200,text=0000,fill="red",font=Mapolice)
###########################################################
########### Receptionnaire d'évènement ####################
###########################################################
Canevas.bind_all('<Right>',joueur_droite)
Canevas.bind_all('<Left>',joueur_gauche)
Canevas.bind_all('<Up>',joueur_haut)
Canevas.bind_all('<Down>',joueur_bas)
##########################################################
############# Programme principal ########################
##########################################################
affichage()
coordonnees_depart()
avance()
###################### FIN ###############################
Mafenetre.mainloop()
