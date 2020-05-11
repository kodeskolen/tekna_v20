# -*- coding: utf-8 -*-
"""
Created on Mon May 11 17:29:37 2020

@author: Marie
"""




kokepunkt = 83 # grader C
frysepunkt = -89 # grader C

temperatur = float(input("Hva er temperaturen?"))

if temperatur  < frysepunkt:
    print("Det er fast stoff")
elif temperatur < kokepunkt:
    print("Det er en væske")
else:
    print("Det er en gass")
    

