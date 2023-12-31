#tree_pattern.py
import random
from math import ceil
rows = int(input("How many Rows: "))
columns = int(input("How many Columns: "))
tree_floors = int(input("How many Tree Floors: "))
while True:
    star_bell_add = int(input("How many Christmas Balls(1-10): "))
    if star_bell_add > 10:
        print("You are not allowed to add more than 10 Christmas Balls")
    elif star_bell_add < 1:
        print("You are not allowed to add less than 1 Christmas Ball")
    else:
        break
while True:
    green_add = int(input("How many Twigs(1-10): "))
    if green_add > 10:
        print("You are not allowed to add more than 10 Twigs")
    elif green_add < 1:
        print("You are not allowed to add less than 1 Twig")
    else:
        break

star_bell = []
for i in range(star_bell_add):
    star_bell.append("🕯 ")
for i in range(green_add):
    star_bell.append("* ")
rows_half = round(rows/2)
columns_half = ceil(columns/2)

def tree_pattern(rows, columns, stars):
    x = list()
    y = list()
    z = "★ "
    for j in range(0, tree_floors):
        rows_floor = round(rows/(tree_floors-j))
        if j < 1:
            for i in range(1, rows_floor):
                for k in range(round(((100/rows)/100)*columns*i)):
                    x.append(random.choice(star_bell))
                if i == 1:
                    print((z).center(columns*2," "))
                else:
                    print("".join(x).center(columns*2," "))
                x.clear()      
        else:
            for i in range(round(rows_floor/3), rows_floor):
                for k in range(round(((100/rows)/100)*columns*(i+1))):
                    y.append(random.choice(star_bell))
                print("".join(y).center(columns*2," "))    
                y.clear()
    for i in range(0, rows_half+1):
        stars = "* " * (columns_half-1)
        print(stars.center(columns*2," "))
tree_pattern(rows, columns,"")