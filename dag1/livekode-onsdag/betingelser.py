# -*- coding: utf-8 -*-
"""
Created on Wed May 13 13:25:15 2020

@author: Marie
"""



kokepunkt = 83 #grader celcius

frysepunkt = -89 # grader celcius

temperatur = float(input("hva er temperaturen?"))

if temperatur < frysepunkt:
    print("Det er fast stoff")
elif temperatur < kokepunkt:
    print("Det er en væske")
else:
    print("Det er en gass")