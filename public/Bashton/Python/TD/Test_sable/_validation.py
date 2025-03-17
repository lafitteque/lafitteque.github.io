# import libraries
import numpy as np
from p5 import *
from basthon.autoeval import (
    Validate,
    ValidateVariables,
    ValidateFunction,
    ValidateFunctionPretty,
)
from itertools import product
import random
# ignore warnings
import warnings

global BLOC, AIR, SABLE
AIR = 0
SABLE = 1
BLOC = 2

def _sable_regle_1(x,y,G,BG,B,BD,D):
    if B == AIR :                            # Règle 1
        return x , y-1
    else :                              # Si la règle 1 ne s'applique pas
        return x , y

def _sable_regle_1_2_a(x,y,G,BG,B,BD,D):
    if  B == AIR :                            # Règle 1
        return x,y-1
    elif BG == AIR :                          # Règle 2 cas & gauche
        return x-1,y-1
    elif BD == AIR :                          # Règle 2 cas à droite
        return x+1, y-1
    else :                              # Si aucune règle ne s'applique
        return x,y


def _sable_regle_1_2_a_hasard(x,y,G,BG,B,BD,D,seed=12345):
    random.seed(seed)
    if  B == AIR :
        return x,y-1
    elif BG == AIR and BD != AIR :
        return x-1 , y-1
    elif BG != AIR and BD == AIR  :
        return x+1 , y-1
    elif BG == AIR and BD == AIR :
        hasard = random.randint(0,1)
        return x + (2*hasard - 1 ) , y-1
    else :
        return x , y


def _sable_regle_1_2_b(x,y,G,BG,B,BD,D,seed=12345):
    random.seed(seed)
    if  B == AIR :                            # Règle 1
        return x,y-1
    elif G == AIR and BG == AIR and (D != AIR or BD != AIR) :                          # Règle 2 cas & gauche
        return x-1,y-1
    elif D == AIR and BD == AIR and (G != AIR or BG != AIR) :                          # Règle 2 cas à droite
        return x+1, y-1
    elif D == AIR and BD == AIR and G == AIR and BG == AIR :
        hasard = random.randint(0,1)
        return x + (2*hasard - 1 ) , y-1
    else :                              # Si aucune règle ne s'applique
        return x,y




########### TESTS ########################

test_imports = ValidateVariables({"var_test_import": 1})

test_simu_1 = ValidateVariables({"simu_1": 1})

test_simu_2 = ValidateVariables({"simu_2": 1})

test_simu_3 = ValidateVariables({"simu_3": 1})

test_simu_4 = ValidateVariables({"simu_4": 1})

test_question_1 = ValidateVariables({"xD": 5,"yD" : 7 , "xG" : 3 , "yG" : 7 , "xB" : 4 , "yB" : 6})

values = [(5,5,0,0,0,0,0), (6,3,0,0,1,0,0),(2,2,1,1,0,1,1),(12,6,1,0,1,0,1),(4,9,0,1,1,0,0),(11,19,0,0,1,1,0),(17,13,0,1,1,1,0)]

test_question_2 = ValidateFunctionPretty("sable_regle_1", values, target_values=[_sable_regle_1(x,y,G,BG,B,BD,D) for x,y,G,BG,B,BD,D in values])


test_question_3 = ValidateFunctionPretty("sable_regle_1_et_2", values, target_values=[_sable_regle_1_2_a(x,y,G,BG,B,BD,D) for x,y,G,BG,B,BD,D in values])


values_seed = [(5,5,0,0,0,0,0,1), (6,3,0,0,1,0,0,2),(2,2,1,1,0,1,1,3),(12,6,1,0,1,0,1,4),(4,9,0,1,1,0,0,5),(11,19,0,0,1,1,0,6),(17,13,0,1,1,1,0,7)]
test_question_4 = ValidateFunctionPretty("q4_seed", values_seed, target_values=[_sable_regle_1_2_a_hasard(x,y,G,BG,B,BD,D,seed) for x,y,G,BG,B,BD,D,seed in values_seed])

test_question_5_a =  ValidateVariables({"x": 3,"y" : 4})

test_question_5_c = ValidateFunctionPretty("q5_seed", values_seed, target_values=[_sable_regle_1_2_b(x,y,G,BG,B,BD,D,seed) for x,y,G,BG,B,BD,D,seed in values_seed])










########### SIMULATION ####################


# Différents états initiaux

def grilleInitialeCarre(nx,ny):
    grille = np.zeros((nx,ny))
    for i in range(max(1,nx//2 - 2), min(nx-1, nx//2 + 2)):
        for j in range(max(1,ny//2 - 2), min(ny-1, ny//2 + 2)):
            grille[i][j] = 1
    return grille

def grilleInitialeVases(nx,ny):
    grille = np.zeros((nx,ny))
    d1,f1,d2,f2,d3,f3 = 2,16,6,24,9,19
    h1,h2,h3 = 16,9,4

    for d,f,h in [(d1,f1,h1) , (d2,f2,h2) , (d3,f3,h3)]:
        grille[d][h+1] = 2
        grille[f][h+1] = 2
        for i in range(d+1,f):
            grille[i][h] = 2

    for i in range(max(1,nx//2 - 7), min(nx-1, nx//2 + 5)):
        for j in range( ny- 6, ny):
            grille[i][j] = 1
    return grille


# Tester la chute
def grilleInitiale1():
    return np.flip([[0, 0, 1, 1, 0],[0, 1, 1, 1, 0],[0, 0, 1, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]).transpose()


# Tester le non écoulement diagonale à travers blocs
def grilleInitiale2():
    return np.flip([[0, 0, 1, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 2, 0, 2, 0],[0, 0, 2, 0, 0]]).transpose()


# Tester les chutes diag
def grilleInitiale3():
    return np.flip([[0, 0, 1, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 2, 0, 0],[0, 2, 2, 2, 0]]).transpose()


def grilleInitialeGrande():
    return np.flip([[2, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1, 1, 1, 2], [2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1, 1, 1, 1, 1, 1, 0, 2], [2, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2], [2, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1,
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2], [2, 0, 0, 0, 0, 0, 1, 0, 1, 1,
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 2], [2, 0, 0, 0, 0, 0,
0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 2], [2, 0,
0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0,
 2], [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
 1, 0, 0, 0, 2], [2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 2, 1, 1, 1, 1,
 1, 1, 1, 1, 0, 0, 1, 0, 2], [2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,
 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 2], [2, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0,
 2, 2, 2, 2, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 2], [2, 0, 0, 0, 0, 0, 0, 2, 2,
 0, 0, 0, 2, 2, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 2], [2, 0, 0, 0, 0,
 0, 0, 0, 2, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], [2,
 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0
, 0, 2], [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0
, 0, 0, 0, 0, 0, 2], [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2
, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2], [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2], [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2], [2, 0, 0, 0, 0, 0, 0, 0
, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2], [2, 0, 0, 0
, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2],
 [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0,
0, 0, 0, 2], [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 2], [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], [2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], [2, 0, 0, 0, 2, 2, 2, 0, 0, 0,
0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], [2, 0, 0, 0, 0, 0,
2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], [2, 0,
0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 2], [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 2], [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]).transpose()





def etapeSuivante(grille,nx,ny,FONCTION_A_APPLIQUER):
        for j in range(1,ny):
            for i in range(1,nx-1):


                if grille[i][j] == SABLE:
                    G,BG,B,BD,D = grille[i-1][j], grille[i-1][j-1], grille[i][j-1], grille[i+1][j-1], grille[i+1][j]
                    nouveaux , nouveauy = FONCTION_A_APPLIQUER(i,j,G,BG,B,BD,D)
                    grille[i][j] = AIR
                    grille[nouveaux][nouveauy] = SABLE

        return grille

def calculToutesFrames(nFrames,nx,ny,FONCTION_A_APPLIQUER, initial = "carre"):
    res = np.zeros((nFrames,nx,ny))
    if initial == "carre":
        res[0] = grilleInitialeCarre(nx,ny)
    elif initial == "vases":
        res[0] = grilleInitialeVases(nx,ny)
    elif initial == "grande":
        nx=30
        ny = 30
        res = np.zeros((nFrames,nx,ny))
        res[0] = grilleInitialeGrande()
    elif initial == 1:
        nx=5
        ny = 5
        res = np.zeros((nFrames,nx,ny))
        res[0] = grilleInitiale1()
    elif initial == 2:
        nx=5
        ny = 5
        res = np.zeros((nFrames,nx,ny))
        res[0] = grilleInitiale2()
    elif initial == 3:
        nx=5
        ny = 5
        res = np.zeros((nFrames,nx,ny))
        res[0] = grilleInitiale3()
    for i in range(1,nFrames):
        res[i] = etapeSuivante(res[i-1],nx,ny,FONCTION_A_APPLIQUER)
    return res,nx


def step(toutesLesFrames,i,size):
    background(255)

    Y = np.flip(toutesLesFrames[i, :, :],1).transpose()

    for row in range(size):
        for col in range(size):
            if Y[row, col] == 0:
                fill(240, 240, 242),
            elif Y[row, col] == 1:
                fill(224, 205, 169)
            else :
                fill(0)
            rect(col * (500 / size), row * (500 / size), 500 / size, 500 / size)
