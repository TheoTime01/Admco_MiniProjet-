#!/usr/bin/env python
# coding: utf-8
"""
author : theotime Perrichet

-Ce code permet de faire des logging des différents fonctions
des packages utilisés
"""
import unittest
import logging

from Package_Robot.Maps import Grid

class TestUp(unittest.TestCase):
    " Test the move_up function of the Grid class"
    def setUp(self):
        self.logger = logging.getLogger()

    def test_move_up(self):
        grid = Grid(20, 20)
        for i in range(20):
            a = grid.move_up()
            if self.assertFalse(a):
                self.logger.info("move_up=>le robot sort de la zone")
                break



class TestDown(unittest.TestCase):
    " Test the move_down function of the Grid class"
    def setUp(self):
        self.logger = logging.getLogger()

    def test_move_down(self):
        grid = Grid(20, 20)
        for i in range(20):
            a = grid.move_up()
            if self.assertFalse(a):
                self.logger.info("move_down=>le robot sort de la zone")
                break


class TestLeft(unittest.TestCase):
    " Test the move_left function of the Grid class"
    def setUp(self):
        self.logger = logging.getLogger()

    def test_move_left(self):
        grid = Grid(20, 20)
        for i in range(20):
            a = grid.move_left()
            if self.assertFalse(a):
                self.logger.info("move_left=>le robot sort de la zone")
                break


class TestRight(unittest.TestCase):
    " Test the move_right function of the Grid class"
    def setUp(self):
        self.logger = logging.getLogger()

    def test_move_right(self):
        grid = Grid(20,20)
        for i in range(20):
            a = grid.move_left()
            if self.assertFalse(a):
                self.logger.info("move_right=>le robot sort de la zone")
                break

class TestGrid(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger()

    def test_grid(self):
        "cette fonction permet de tester la taille limite max de la grille"
        grid = Grid(50, 50)
        if self.assertTrue(grid.nb_lines > 20 or grid.nb_columns > 20):
            self.logger.info("Grid(50,50)=>la grille est trop grande")
    
    def test_grid_inf_un(self):
        "cette fonction permet de tester la taille limite min de la grille"
        grid = Grid(0, 0)
        if self.assertTrue(grid.nb_lines < 1 or grid.nb_columns < 1):
            self.logger.info("Grid(0,0)=>la grille est trop petite")

    def test_grid_charactere(self):
        "cette fonction permet de tester si les entrées sont des caractères"
        grid = Grid("a", "b")
        if self.assertTrue(type(grid.nb_lines) != int or type(grid.nb_columns) != int):
            self.logger.info("Grid(a,b)=>les caractères ne sont pas des entiers")

    def test_grid_float(self):
        "cette fonction permet de tester si les entrées sont des floats"
        grid = Grid(1.5, 2.5)
        if self.assertTrue(type(grid.nb_lines) != int or type(grid.nb_columns) != int):
            self.logger.info("Grid(1.5,2.5)=>les floats ne sont pas des entiers")