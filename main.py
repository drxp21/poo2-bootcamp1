import random as rand
import os
from threading import Timer
import LetGet as game





motsFile = open('mots.txt')
mots=list(motsFile.read().split("\n"))

voyelles = ['a', 'o', 'i', 'u', 'e', 'y']

uniques=0


ToBeFound=''

MotsFiltered=list

print('Bienvenue sur Let-Get \n ')
niveau=int(input('Choisissez votre niveau (entre 1 et 3)'))

ToBeFound=game.chooseWord(mots,niveau)

print(f'Vous avez choisis le niveau {niveau}')

print(f' Je vous propose un mot de {len(ToBeFound)} lettres. De quel mot s’agit-il ? \n ######################################################################### \n')


def exitfunc():
    print(f"Le temps est ecoulé . Le mot a trouver etait '{ToBeFound}'")
    os._exit(0)
Timer(120, exitfunc).start() #le jeu s'arrete en 2 minutes


for l in ToBeFound:
    if ToBeFound.count(l)==1:
        uniques+=1
        
letter = []
tentatives = 0
pt_erreur = 3
found = False

while not found:
    found = True
    for l in ToBeFound:
        if l in letter:
            print(l, end=" ")
        else:
            found = False
            print("_", end=" ")

    if tentatives == 6:
        print("\nVous avez perdu!")
        print(f"\nLe mot a jouer etait '{ToBeFound}'")
        os._exit(0)
    else:

        if found:
            print("\nFelicitation vous avez gagné!!!")
            game.calculScore(tentatives,uniques)
            game.saveScore(tentatives,uniques)
            # ecrire dans score.txt

            os._exit(0)
        entree = input("\nEntrez une lettre:  \n")

        letter.append(entree)
        if ((len(entree)>1) or (not(entree.isalpha()))):
            print("Vous devez entrer une seule lettre de l'alphabet a la fois \n")
            pt_erreur -= 1
            print(f"\n Il vous reste: {pt_erreur} points erreur")
            if(pt_erreur == 0):
                tentatives +=1
                print(f'Vous perdez une tentative. Il vous reste {6-tentatives} tentatives \n')
                pt_erreur=3
            
        elif entree not in ToBeFound:
            print('Cette lettre ne fait pas partie du mot \n')
            if entree in voyelles:
                tentatives += 2
            else:
                tentatives += 1

            game.pendu(tentatives)       
        





