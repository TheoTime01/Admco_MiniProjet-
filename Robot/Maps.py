#!/usr/bin/env python
# coding: utf-8
"""
author : theotime Perrichet

-Ce code définit une classe  qui fait des opérations arithmétiques avec des complexes
"""

#we create a Grid
#We use a 1 in the grid to represent the presence of a robot. At the beginning the robot is at position 0,0 of the grid. 
#The methods allow to move the robot. In case of impossibility to move (presence of an edge) the robot stays at its place. 
# The call of the method returns True if the move is possible and False in the opposite case.   
#The method display allows to display the grid.

class Grid:
    def __init__(self, nb_lines, nb_columns):
        self.nb_lines = nb_lines
        self.nb_columns = nb_columns
        self.grid = [[0 for i in range(nb_lines)] for j in range(nb_columns)]
        self.grid[0][0] = 1
        self.x = 0
        self.y = 0

    def move_up(self):
        if self.y == 0:
            return False
        else:
            self.grid[self.y][self.x] = 0
            self.y -= 1
            self.grid[self.y][self.x] = 1
            return True

    def move_down(self):
        if self.y == self.nb_columns-1:
            return False
        else:
            self.grid[self.y][self.x] = 0
            self.y += 1
            self.grid[self.y][self.x] = 1
            return True

    def move_right(self):
        if self.x == self.nb_lines-1:
            return False
        else:
            self.grid[self.y][self.x] = 0
            self.x += 1
            self.grid[self.y][self.x] = 1
            return True

    def move_left(self):
        if self.x == 0:
            return False
        else:
            self.grid[self.y][self.x] = 0
            self.x -= 1
            self.grid[self.y][self.x] = 1
            return True

    def display(self):
        for i in range(self.nb_columns):
            print(self.grid[i])
        print()


if __name__=="__main__":
    grid = Grid(10,10)
    grid.display()
    grid.move_up()
    grid.display()
    grid.move_down()
    grid.display()
    grid.move_right()
    grid.display()
    grid.move_left()
    grid.display()
    