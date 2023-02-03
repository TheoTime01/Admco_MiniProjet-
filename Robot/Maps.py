#!/usr/bin/env python
# coding: utf-8
"""
author : theotime Perrichet

-Ce code définit une classe  qui fait des opérations arithmétiques avec des complexes
"""

class Grid:
    def __init__(self, nb_lines, nb_columns):
        # Initialise the grid with nb_lines lines and nb_columns columns
        self.nb_lines = nb_lines
        self.nb_columns = nb_columns
        self.grid = [[0 for i in range(nb_lines)] for j in range(nb_columns)]
        # Put a 1 on the first cell of the grid
        self.grid[0][0] = 1
        # Initialise the position of the robot
        self.x = 0
        self.y = 0
        #the grid cannot depass 50 lines and 50 columns
        if self.nb_lines > 20 or self.nb_columns > 20:
            raise ValueError("The grid cannot have more than 50 lines or 50 columns")


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
    grid = Grid(20,20)
    grid.display()
    grid.move_up()
    grid.display()
    grid.move_down()
    grid.display()
    grid.move_right()
    grid.display()
    grid.move_left()
    grid.display()
