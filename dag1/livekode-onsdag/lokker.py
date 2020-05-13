# -*- coding: utf-8 -*-
"""
Created on Wed May 13 14:07:38 2020

@author: Marie
"""

# En petriskål har 2 bakterier. 
# Bakteriene øker med 30% hver time
# Hvor mange bakterier er det etter
# 10 timer?

antall_timer = 10

vekstfaktor = 1.3

bakterie_mengde = 2

for time in range(antall_timer):
    bakterie_mengde *= vekstfaktor
    
    print(bakterie_mengde)