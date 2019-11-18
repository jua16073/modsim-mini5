import os
import math
import time
#import pygame
from random import randint


#el sarandeo
poco_derecha = lambda g: (1/15) * g['angle'] if(g['angle'] >= 0 and g['angle'] < 15) else 1 if(g['angle'] >= 15 and g['angle'] <= 30) else (-1/15) * g['angle'] + 3 if(g['angle'] > 30 and g['angle'] <= 45) else 0
mucho_derecha = lambda g: (1/15) * g['angle'] - 3 if(g['angle'] > 45 and g['angle'] < 60) else 1 if (g['angle'] >= 60 and g['angle'] <= 85) else (1/5) * g['angle'] + 18 if(g['angle'] > 85 and g['angle'] <= 90) else 0
poco_izquierda = lambda g: (1/15) * g['angle'] - 21 if (g['angle'] > 315 and g['angle'] <330) else 1 if (g['angle'] >= 330 and g['angle'] <= 345) else (-1/15) * g['angle'] + 24 if(g['angle'] > 345 and g['angle'] <= 360) else 0
mucho_izquierda = lambda g: (1/15) * g['angle'] - 18 if (g['angle'] >= 270 and g['angle'] < 285) else 1 if (g['angle']>= 285 and g['angle'] <= 300) else (-1/15) * g['angle'] + 21 if (g['angle'] > 300 and g['angle'] <= 315) else 0

#el lejaneo
cerquita = lambda d: (-1/9) * d['dist'] - (1/9) if(d['dist'] >= 1 and d['dist'] <= 10) else 0
lejitos = lambda d: (1/10) * d['dist'] + 4 if(d['dist'] > 30 and d['dist'] <= 40 ) else 0
mediomedio = lambda d: (1/10) * d['dist'] - 1 if(d['dist'] > 10 and d['dist'] <= 20) else (-1/10) * d['dist'] + 3 if(d['dist'] > 20 and d['dist'] <= 30) else 0

#pertenencia
rotar_poco_derecha = lambda p: 1 if(p['rotate'] > 0 and p['rotate'] <= 35) else (-1/55) * p['rotate'] + (18/11) if(p['rotate'] > 35 and p['rotate'] < 90) else 0
rotar_mucho_derecho = lambda p: 1 if(p['rotate'] > 35) else 0
rotar_poco_izquierda = lambda p: 1 if(p['rotate'] < 360 and p['rotate'] > 325) else (1/55) * p['rotate'] - (54/11) if( p['rotate'] < 325 and p['rotate'] > 270) else 0
rotar_mucho_izquierda = lambda p: 1 if(p['rotate'] > 325) else 0


#fuzzy shit
def fuzzy_or(l1, l2):
    def anon(diccionario):
        return max(l1(diccionario), l2(diccionario))
    return anon

def fuzzy_and(l1, l2):
    def anon(diccionario):
        return min(l1(diccionario), l2(diccionario))
    return anon

hypothesis = fuzzy_or(mucho_izquierda, poco_izquierda)
hypothesis2 = fuzzy_or(mucho_derecha, poco_derecha)
hypothesis3 = fuzzy_or(poco_derecha, poco_izquierda)

clausula1 = fuzzy_and(hypothesis, rotar_poco_izquierda)
clausula2 = fuzzy_and(hypothesis, mucho_izquierda)
clausula3 = fuzzy_and(hypothesis2, rotar_poco_derecha)
clausula4 = fuzzy_and(hypothesis2, mucho_derecha)
clausula5 = fuzzy_and(hypothesis3, rotar_poco_derecha)
clausula6 = fuzzy_and(hypothesis3, rotar_poco_izquierda)

help1 = fuzzy_or(clausula1, clausula2)
help2 = fuzzy_or(help1, clausula3)
help3 = fuzzy_or(help2, clausula4)
help4 = fuzzy_or(help3, clausula5)
help5 = fuzzy_or(help4, clausula6)

def choose(data, key, clause):
    t = 0
    b = 0
    for i in range(1, 90, 1):
        data[key] = i
        u = clause(data)
        t += i * u
        b += u
        data[key] = i +270
        u = clause(data)
        t += i * u
        b += u

    return t/b

print(choose({"angle": 53}, "rotate", help5))