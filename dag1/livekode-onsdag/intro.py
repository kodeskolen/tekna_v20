# -*- coding: utf-8 -*-
"""
Created on Wed May 13 12:46:42 2020

@author: Marie
"""

konsentrasjon = 0.009 # mol/L sukker i menneskeblod

antall_liter = 2.5 # L blod i menneske

mengde = konsentrasjon*antall_liter

print(f"Hvis et menneske har {konsentrasjon} mol/L")
print(f'og {antall_liter} liter blod')
print(f'har det {mengde} mol med sukker i blodet sitt')
