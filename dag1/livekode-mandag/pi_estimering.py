# -*- coding: utf-8 -*-
"""
Created on Mon May 11 19:18:46 2020

@author: Marie
"""

from pylab import uniform, sqrt

def kast_dart():
    # kast en tilfeldig dart
    x_koordinat = uniform(-1, 1)
    y_koordinat = uniform(-1, 1)
    return x_koordinat, y_koordinat

def pytagoras(katet1, katet2):
    # tar inn to kateter i rettvinklet trekant
    # returner tilhørende hypotenus
    return sqrt(katet1**2 + katet2**2)

def traff_blinken(dart_x, dart_y):
    # ta inn koordinater til et dartkast
    # returnere True dersom darten traff
    # False hvis ikke
    
    avstand_origo = pytagoras(dart_x, dart_y)
    if avstand_origo < 1:
        return True
    else:
        return False

antall_kast = 10000

antall_treff = 0

for kast in range(antall_kast):
    #kast en pil
    dart_x, dart_y = kast_dart()
    
    #sjekk treff
    if traff_blinken(dart_x, dart_y):
        antall_treff += 1
        
estimert_sannsynlighet = antall_treff/antall_kast
estimert_pi = 4*estimert_sannsynlighet

print(f'Antall kast: {antall_kast}')
print(f'Antall treff: {antall_treff}')
print(f'Sannsynlighet: {estimert_sannsynlighet}')
print(f'Estimert pi: {estimert_pi}')