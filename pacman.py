########## Importer les modules necessaires ##############
from tkinter import *
from tkinter.font import Font
from random import *
import time
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
        x=480 #on revient à gauche
        y+=50 #une ligne en dessous

def coordonnees_depart(): #coordonnees de départ du joueur et des ennemis.
    global coos_joueur, coos_ennemis, joueur, ennemi1, ennemi2, ennemi3, ennemi4
    joueur=Canevas.create_oval(coos_joueur[0],coos_joueur[1],fill='yellow')
    ennemi1=Canevas.create_polygon(coos_ennemis[0][0],coos_ennemis[0][1],coos_ennemis[0][2],fill='brown')
    ennemi2=Canevas.create_polygon(coos_ennemis[1][0],coos_ennemis[1][1],coos_ennemis[1][2],fill='brown')
    ennemi3=Canevas.create_polygon(coos_ennemis[2][0],coos_ennemis[2][1],coos_ennemis[2][2],fill='brown')
    ennemi4=Canevas.create_polygon(coos_ennemis[3][0],coos_ennemis[3][1],coos_ennemis[3][2],fill='brown')

def joueur_droite(ev=None): #si touche droite cliquée
    global direction_joueur
    if direction_joueur!='droite': #si on n'avance pas déjà à droite, on met la variable direction_joueur sur 'droite'
        direction_joueur='droite'

def joueur_gauche(ev=None): #si touche gauche cliquée
    global direction_joueur
    if direction_joueur!='gauche': #si on n'avance pas déjà à gauche, on met la variable direction_joueur sur 'gauche'
        direction_joueur='gauche'

def joueur_haut(ev=None): #si touche haut cliquée
    global direction_joueur
    if direction_joueur!='haut': #si on n'avance pas déjà en haut, on met la variable direction_joueur sur 'haut'
        direction_joueur='haut'

def joueur_bas(ev=None): #si touche bas cliquée
    global direction_joueur
    if direction_joueur!='bas': #si on n'avance pas déjà en bas, on met la variable direction_joueur sur 'bas'
        direction_joueur='bas'

def joueur_avance():
    global deuxieme_couche, varScore
    [a,b,c,d] = Canevas.coords(joueur) #a,b=coordonnées x y en haut à gauche du joueur / c,d=coordonnées x y en bas à droite du joueur
    i = conversion(a,b)[0] #coordonnées i du joueur
    j = conversion(a,b)[1] #coordonnées j du joueur
    Canevas.delete(deuxieme_couche) #on supprime la deuxième couche présente sur le joueur s'il y en a une
    if direction_joueur=='droite':
        if donnees_cases[j][i+1]!=3: #si pas de mur, avance
            Canevas.coords(joueur,a+50,b,c+50,d)
            if donnees_cases[j][i]==1: #si  piece : ramasse
                varScore=str(int(varScore)+1) #on rajoute un au score
                if len(varScore)==1: #s'il n'y a qu'un chiffre dans le score, on rajoute un 0 à gauche
                    varScore='0'+varScore
                score() #on modifie le score
                donnees_cases[j][i]=0 #remplace par du vide
                Canevas.create_oval(a+20,b+20,c-20,d-20,fill='black')
    if direction_joueur=='gauche':
        if donnees_cases[j][i-1]!=3:
            Canevas.coords(joueur,a-50,b,c-50,d)
            if donnees_cases[j][i]==1: #si  piece : ramasse
                varScore=str(int(varScore)+1) #on rajoute un au score
                if len(varScore)==1: #s'il n'y a qu'un chiffre dans le score, on rajoute un 0 à gauche
                    varScore='0'+varScore
                score() #on modifie le score
                donnees_cases[j][i]=0 #remplace par du vide
                Canevas.create_oval(a+20,b+20,c-20,d-20,fill='black')
    if direction_joueur=='haut':
        if donnees_cases[j-1][i]!=3:
            Canevas.coords(joueur,a,b-50,c,d-50)
            if donnees_cases[j][i]==1: #si  piece : ramasse
                varScore=str(int(varScore)+1) #on rajoute un au score
                if len(varScore)==1: #s'il n'y a qu'un chiffre dans le score, on rajoute un 0 à gauche
                    varScore='0'+varScore
                score() #on modifie le score
                donnees_cases[j][i]=0 #remplace par du vide
                Canevas.create_oval(a+20,b+20,c-20,d-20,fill='black')
    if direction_joueur=='bas':
        if donnees_cases[j+1][i]!=3:
            Canevas.coords(joueur,a,b+50,c,d+50)
            if donnees_cases[j][i]==1: #si  piece : ramasse
                varScore=str(int(varScore)+1) #on rajoute un au score
                if len(varScore)==1: #s'il n'y a qu'un chiffre dans le score, on rajoute un 0 à gauche
                    varScore='0'+varScore
                score() #on modifie le score
                donnees_cases[j][i]=0 #remplace par du vide
                Canevas.create_oval(a+20,b+20,c-20,d-20,fill='black')
    [a,b,c,d]=Canevas.coords(joueur) #on prend les nouvelles coordonnées x y du joueur
    if donnees_cases[j][i]==0: #si le joueur est sur une case vide, il est nécessaire d'appliquer un autre oval jaune sur le joueur pour ne pas voir l'oval noir (quand la pièce a été ramassée)
        deuxieme_couche=Canevas.create_oval(a+5,b+5,c-5,d-5,fill="yellow",outline="")
    Canevas.update()
    Mafenetre.after(200, joueur_avance) #on relance la fonction

def ennemis_avancent(): #A FINIR (la fonction marche passs)
    global coos_ennemis, ennemi1, ennemi2, ennemi3, ennemi4
    [e1,f1,g1,h1] = Canevas.coords(ennemi1) #e,f=coordonnées x y en haut à gauche de l'ennemi / g,h=coordonnées x y en bas à droite de l'ennemi
    [e2,f2,g2,h2] = Canevas.coords(ennemi2)
    [e3,f3,g3,h3] = Canevas.coords(ennemi3)
    [e4,f4,g4,h4] = Canevas.coords(ennemi4)
    ennemis_IJ=[] #liste des coordonnées i et j des ennemis
    ennemis_IJ.append(conversion(e1,f1)) #ajout des coordonnées i et j de l'ennemi 1
    ennemis_IJ.append(conversion(e2,f2)) #ajout des coordonnées i et j de l'ennemi 2
    ennemis_IJ.append(conversion(e3,f3)) #ajout des coordonnées i et j de l'ennemi 3
    ennemis_IJ.append(conversion(e4,f4)) #ajout des coordonnées i et j de l'ennemi 4
    for e in ennemis_IJ:
        direction_ennemi=random.choice(['droite', 'gauche', 'haut', 'bas'])
        if direction_ennemi=='droite':
            if donnees_cases[e[1]][e[0]+1]!=3: #si pas de mur, avance
                print(0)


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

def score(): #augmentation score
    global chiffre_score
    Canevas.delete(chiffre_score)
    chiffre_score=Canevas.create_text(1300,75,text=varScore,fill="red",font=Mapolice)

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

direction_joueur=None

deuxieme_couche=None

varScore='00'

chiffre_score=None
#########################################################
########## Interface graphique ##########################
##########################################################
Mafenetre = Tk()
Mafenetre.title("Titre")
Canevas = Canvas(Mafenetre,width=1920,height=1080,bg ='black')
#Mafenetre.attributes("-fullscreen", True)
Canevas.pack()
Mapolice = Font(family='Auto Digital', size=40)
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
joueur_avance()

#score :
Canevas.create_text(1190,75,text="Score:",fill="red",font=Mapolice)
chiffre_score=Canevas.create_text(1300,75,text=varScore,fill="red",font=Mapolice)
Canevas.create_text(1382,75,text="/99",fill="red",font=Mapolice)
###################### FIN ###############################
Mafenetre.mainloop()
