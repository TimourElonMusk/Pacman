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

def coordonnees_depart(): #coordonnees de départ du joueur et des ennemis.
    global coos_joueur, coos_ennemis, joueur, ennemi1, ennemi2, ennemi3, ennemi4
    joueur=Canevas.create_oval(coos_joueur[0],coos_joueur[1],fill='yellow')
    ennemi1=Canevas.create_polygon(coos_ennemis[0][0],coos_ennemis[0][1],coos_ennemis[0][2],fill='brown')
    ennemi2=Canevas.create_polygon(coos_ennemis[1][0],coos_ennemis[1][1],coos_ennemis[1][2],fill='brown')
    ennemi3=Canevas.create_polygon(coos_ennemis[2][0],coos_ennemis[2][1],coos_ennemis[2][2],fill='brown')
    ennemi4=Canevas.create_polygon(coos_ennemis[3][0],coos_ennemis[3][1],coos_ennemis[3][2],fill='brown')

def joueur_droite(ev=None):
    global direction
    if direction!='droite':
        direction='droite'
        avance()

def joueur_gauche(ev=None):
    global direction
    if direction!='gauche':
        direction='gauche'
        avance()

def joueur_haut(ev=None):
    global direction
    if direction!='haut':
        direction='haut'
        avance()

def joueur_bas(ev=None):
    global direction
    if direction!='bas':
        direction='bas'
        avance()

def avance():
    if direction=='droite':
        [a,b,c,d] = Canevas.coords(joueur)
        Canevas.coords(joueur,a+4,b,c+4,d)
        touche_mur(a,b,c,d)
        Mafenetre.after(2, avance)
    if direction=='gauche':
        [a,b,c,d] = Canevas.coords(joueur)
        Canevas.coords(joueur,a-4,b,c-4,d)
        touche_mur(a,b,c,d)
        Mafenetre.after(2, avance)
    if direction=='haut':
        [a,b,c,d] = Canevas.coords(joueur)
        Canevas.coords(joueur,a,b-4,c,d-4)
        touche_mur(a,b,c,d)
        Mafenetre.after(2, avance)
    if direction=='bas':
        [a,b,c,d] = Canevas.coords(joueur)
        Canevas.coords(joueur,a,b+4,c,d+4)
        touche_mur(a,b,c,d)
        Mafenetre.after(2, avance)

def touche_mur(a,b,c,d):
    global direction
    #droite
    if ((conversion(a+1,b+1)[0]==3 and ((conversion(c+1,d+1)[1]>=4 and conversion(a+1,b+1)[1]<=7) or (conversion(c+1,d+1)[1]>=10 and conversion(a+1,b+1)[1]<=13))) or (conversion(a+1,b+1)[0]==9 and ((conversion(c+1,d+1)[1]>=2 and conversion(a+1,b+1)[1]<=7) or (conversion(c+1,d+1)[1]>=10 and conversion(a+1,b+1)[1]<=15))) or (conversion(a+1,b+1)[0]==13 and ((conversion(c+1,d+1)[1]>=4 and conversion(a+1,b+1)[1]<=7) or (conversion(c+1,d+1)[1]>=10 and conversion(a+1,b+1)[1]<=13))) or conversion(a+1,b+1)[0]==19) and direction=='droite':
        Canevas.coords(joueur,a-2,b,c-2,d)
        direction=None
    #gauche
    if (conversion(c,d)[0]==2 or (conversion(c,d)[0]==8 and ((conversion(c,d)[1]>=4 and conversion(a+0.1,b+0.1)[1]<=7) or (conversion(c,d)[1]>=10 and conversion(a+0.1,b+0.1)[1]<=13))) or (conversion(a+1,b+1)[0]==11 and ((conversion(c+1,d+1)[1]>=2 and conversion(a+1,b+1)[1]<=7) or (conversion(c+1,d+1)[1]>=10 and conversion(a+1,b+1)[1]<=15))) or (conversion(c,d)[0]==18 and ((conversion(c,d)[1]>=4 and conversion(a+0.1,b+0.1)[1]<=7) or (conversion(c,d)[1]>=10 and conversion(a+0.1,b+0.1)[1]<=13)))) and direction=='gauche':
        Canevas.coords(joueur,a+2,b,c+2,d)
        direction=None
    #haut
    if (conversion(c,d)[1]==2 or ((conversion(c,d)[0]>=4 and conversion(a,b)[0]<=7) and (conversion(c,d)[1]==8 or conversion(c,d)[1]==14)) or (((conversion(c,d)[0]==8 or conversion(c,d)[0]==9) or (conversion(c,d)[0]==12 or conversion(c,d)[0]==13)) and conversion(c,d)[1]==12) or ((conversion(c,d)[0]>=14 and conversion(a,b)[0]<=17) and (conversion(c,d)[1]==8 or conversion(c,d)[1]==14)) or (((conversion(c,d)[0]==10) or (conversion(c,d)[0]==11)) and conversion(c,d)[1]==8) or (conversion(a,b)[0]==11 and conversion(c,d)[1]==8)) and direction=='haut':
        Canevas.coords(joueur,a,b+2,c,d+2)
        direction=None
    #bas
    if (((conversion(c,d)[0]>=4 and conversion(a,b)[0]<=7) and (conversion(a,b)[1]==3 or conversion(a+0.1,b+0.1)[1]==9)) or ((conversion(a+0.1,b+0.1)[0]>=8 and conversion(a+0.1,b+0.1)[0]<=13) and conversion(a+2.1,b+2.1)[1]==9) or ((conversion(c,d)[0]>=14 and conversion(a,b)[0]<=17) and (conversion(a,b)[1]==3 or conversion(a+0.1,b+0.1)[1]==9)) or conversion(a,b)[1]==15) and direction=='bas':
        Canevas.coords(joueur,a,b-2,c,d-2)
        direction=None

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
font = Font(family='Arial', size=200)
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
###################### FIN ###############################
Mafenetre.mainloop()
