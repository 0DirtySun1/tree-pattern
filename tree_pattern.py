#tree_pattern.py
import queue
import random
from math import ceil
rows = int(input("Wie viele Reihen: "))
columns = int(input("Wie viele Spalten: "))
tree_floors = int(input("Wie viele Abstufungen: "))
rows_half = round(rows/2)
columns_half = ceil(columns/2)
star_bell = ["* ", "o "]

def tree_pattern(rows, columns):
    stars = ""
    x = ""
    for j in range(0, tree_floors):
        rows_floor = round(rows/(tree_floors-j))
        if j < 1:
            for i in range(1, rows_floor):
                stars = "* " * round(((100/rows)/100)*columns*i)
                if stars > "* " * columns:
                    print("* " * columns)
                else:
                    print(stars.center(columns*2," "))    
                        
        else:
            for i in range(round(rows_floor/3), rows_floor):
                stars = "* " * round(((100/rows)/100)*columns*i)
                if stars > "* " * columns:
                    print("* " * columns)
                else:
                    print(stars.center(columns*2," "))            
    for i in range(0, rows_half+1):
        stars = "* " * (columns_half-1)
        print(stars.center(columns*2," "))
tree_pattern(rows, columns)