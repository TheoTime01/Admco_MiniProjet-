#!/usr/bin/env python
# coding: utf-8
"""
author : theotime Perrichet

-Ce code définit une classe  qui fait des opérations arithmétiques avec des complexes
"""
import random
class Grid:
    def __init__(self, nb_lines, nb_columns):
        "Initialise la grille avec nb_lines lignes et nb_columns colonnes"
        # Initialise the grid with nb_lines lines and nb_columns columns
        self.nb_lines = nb_lines
        self.nb_columns = nb_columns
        #the grid cannot depass 50 lines and 50 columns
        if self.nb_lines > 20 or self.nb_columns > 20:
            raise ValueError("La grille ne peut pas dépasser 20 lignes et 20 colonnes")
        elif self.nb_lines < 1 or self.nb_columns < 1:
            raise ValueError("La grille doit avoir au moins une ligne et une colonne")
        elif type(self.nb_lines) != int or type(self.nb_columns) != int:
            raise ValueError("La grille doit être un entier")
        else:
            self.grid = [[0 for i in range(nb_lines)] for j in range(nb_columns)]



    def move_up(self):
        "cette fonction permet de faire bouger le robot vers le haut"
        if self.y == 0:
            return False
        else:
            self.grid[self.y][self.x] = 0 
            self.y -= 1
            self.grid[self.y][self.x] = 1
            return True

    def move_down(self):
        "cette fonction permet de faire bouger le robot vers le bas"
        if self.y == self.nb_columns-1:
            return False
        else:
            self.grid[self.y][self.x] = 0
            self.y += 1
            self.grid[self.y][self.x] = 1
            return True

    def move_right(self):
        "cette fonction permet de faire bouger le robot vers la droite"
        if self.x == self.nb_lines-1:
            return False
        else:
            self.grid[self.y][self.x] = 0
            self.x += 1
            self.grid[self.y][self.x] = 1
            return True

    def move_left(self):
        "cette fonction permet de faire bouger le robot vers la gauche"
        if self.x == 0:
            return False
        else:
            self.grid[self.y][self.x] = 0
            self.x -= 1
            self.grid[self.y][self.x] = 1
            return True

    def display(self):
        "cette fonction permet d'afficher la grille"
        for i in range(self.nb_columns):
            print(self.grid[i])
        print()
    
    def obstacles(self, nb):
        "cette fonction permet de mettre des obstacles de façon aléatoire sur la grille"
        #the number of obstacles cannot exceed 20
        if nb > 20:
            raise ValueError("Le nombre d'obstacles ne peut pas dépasser 20")
        elif nb < 0:
            raise ValueError("Le nombre d'obstacles doit être positif")
        elif type(nb) != int:
            raise ValueError("Le nombre d'obstacles doit être un entier")
        else:
            for i in range(nb):
                self.grid[random.randint(0, self.nb_columns-1)][random.randint(0, self.nb_lines-1)] = "x"
        #si le robot est sur un obstacle, il ne bouge pas
    





if __name__=="__main__":
    grid = Grid(5,5)
    grid.display()
    grid.move_down()
    grid.display()
    grid.move_down()
    grid.display()
    grid.move_down()
    grid.display()
    grid.move_down()
    grid.display()
