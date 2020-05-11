# -*- coding: utf-8 -*-
"""
Created on Mon May 11 18:15:51 2020

@author: Marie
"""


# En petriskål har 2 bakterier. Bakteriemengden øker med 30% hver time. 
# Hvor mange bakterier er det etter 10 timer?

antall_timer = 10

vekstfaktor = 1.3

bakteriemengde = 2

for time in range(antall_timer):
    bakteriemengde *= vekstfaktor
print(f" {bakteriemengde:.2f}")

