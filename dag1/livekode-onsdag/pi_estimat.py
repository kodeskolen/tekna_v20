# -*- coding: utf-8 -*-
"""
Created on Wed May 13 15:10:24 2020

@author: Marie
"""



from pylab import uniform, sqrt, plot, show, axis, pause, xlim, ylim

def kast_dart():
    # kast en tilfeldig dart
    # returnerer koordinatene til kastet
    # x og y skal være mellom -1 og 1
    x_koordinat = uniform(-1, 1)
    y_koordinat = uniform(-1, 1)
    return x_koordinat, y_koordinat

def pytagoras(katet1, katet2):
    return sqrt(katet1**2 + katet2**2)

def traff_blinken(dart_x, dart_y):
    # Tar inn koordinater til dartkast
    # returnere True dersom darten traff
    # False dersom den ikke traff
    avstand_origo = pytagoras(dart_x, dart_y)
    if avstand_origo < 1:
        return True
    else:
        return False

antall_kast = 1000
antall_treff = 0

for kast in range(antall_kast):
    # kast en dart
    dart_x, dart_y = kast_dart()
    # Sjekk treff
    xlim(-1, 1)
    ylim(-1, 1)
    if traff_blinken(dart_x, dart_y):
        plot(dart_x, dart_y, 'gx')
        antall_treff += 1
    else:
        plot(dart_x, dart_y, 'rx')
    pause(1)
        
estimert_sannsynlighet = antall_treff/antall_kast
estimert_pi = estimert_sannsynlighet*4
axis('equal')
show()
print(f'Antall kast: {antall_kast}')
print(f'Antall treff: {antall_treff}')
print(f'Estimert sannsynlighet: {estimert_sannsynlighet}')
print(f'Estimert pi: {estimert_pi}')