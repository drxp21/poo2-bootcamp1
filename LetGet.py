import random as rand
import os
from threading import Timer

def chooseWord(mots,niveau):
    MotsFiltered=list
    ToBeFound=''
    while True:
        
        match niveau:
            case 1:
                MotsFiltered = list(filter(lambda mot: 2<len(mot)<=4, mots))
                return MotsFiltered[rand.randint(0,len(MotsFiltered)-1)]
            case 2:
                MotsFiltered = list(filter(lambda mot: 4<len(mot)<=7, mots))
                return MotsFiltered[rand.randint(0,len(MotsFiltered)-1)]
            case 3:
                MotsFiltered = list(filter(lambda mot: len(mot)>7, mots))
                return MotsFiltered[rand.randint(0,len(MotsFiltered)-1)]
    

def calculScore(tentatives,uniques):
    print("Votre score est de ", (6-tentatives) * uniques," point(s)")

def saveScore(tentatives,uniques):
    score= (6-tentatives)*uniques
    partieNo=0
    with open('score.txt', 'r') as f:
        # file = f.readlines()
        partieNo=(int(list(f.readlines())[-1].split('|')[1])+1)
        
    with open('score.txt', 'r+') as f:
        lines = f.readlines()

    if len(lines) > int(0) and score>int(lines[0].split(':')[1]):
        lines[0] = f'Meilleur score: {score} \n'

    with open('score.txt', 'w') as file:
        file.writelines( lines )
        file.writelines(f'| {partieNo}      | {6-tentatives}          | {score}     \n')


    # with open('score.txt', 'w') as f:
    #     fi=f.readlines()
    #     if score>int(fi[0].split(':')[1]):
    #         # f.truncate(0)
    #         fi[0] = f"Meilleur score : {score} \n"
    #         f.writelines(fi)
    #         # f.write("".join(fi))
        
    #     f.writelines(f"| {partieNo}     | {6-tentatives}     | {score}    ")

def pendu(cpt):
    match cpt:
        case 1:
            print(f'Vous perdez deux tentative. Il vous reste {6-cpt} tentatives \n')
            print(" |¯¯¯¯¯¯¯¯¯¯¯|")
            print(" |           O")
            print(" |         ")
            print(" |         ")
            print(" |")
            print("-|----------- \n")
        case 2:
            print(f'Vous perdez deux tentative. Il vous reste {6-cpt} tentatives \n')
            print(" |¯¯¯¯¯¯¯¯¯¯¯|")
            print(" |           O")
            print(" |          /")
            print(" |          ")
            print(" |")
            print("-|----------- \n")
        case 3:
            print(f'Vous perdez deux tentative. Il vous reste {6-cpt} tentatives \n')
            print(" |¯¯¯¯¯¯¯¯¯¯¯|")
            print(" |           O")
            print(" |          /|")
            print(" |          ")
            print(" |")
            print("-|----------- \n")
        case 4:
            print(f'Vous perdez deux tentative. Il vous reste {6-cpt} tentatives \n')
            print(" |¯¯¯¯¯¯¯¯¯¯¯|")
            print(" |           O")
            print(" |          /|\\")
            print(" |          ")
            print(" |")
            print("-|----------- \n")    
        case 5:
            print(f'Vous perdez deux tentative. Il vous reste {6-cpt} tentatives \n')
            print(" |¯¯¯¯¯¯¯¯¯¯¯|")
            print(" |           O")
            print(" |          /|\\")
            print(" |          /")
            print(" |")
            print("-|----------- \n")
        case 6:
            print(f'Vous perdez deux tentative. Il vous reste {6-cpt} tentatives \n')
            print(" |¯¯¯¯¯¯¯¯¯¯¯|")
            print(" |           O")
            print(" |          /|\\")
            print(" |          / \\")
            print(" |")
            print("-|----------- \n")

