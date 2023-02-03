#!/usr/bin/env python
# coding: utf-8
"""
author : theotime Perrichet

-Ce code permet de faire des logging des différents fonctions
des packages utilisés
"""
import unittest
import logging

from Robot.Maps import Grid

class Test_move_up(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger()

    def test_move_up(self):
        grid = Grid(5, 5)
        for i in range(5):
            a = grid.move_up()
            if self.assertFalse(a):
                self.logger.info("The robot leaves the zone")
                break



class Test_move_down(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger()

    def test_move_down(self):
        grid = Grid(5, 5)
        for i in range(5):
            a = grid.move_up()
            if self.assertFalse(a):
                self.logger.info("The robot leaves the zone")
                break


class Test_move_left(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger()

    def test_move_left(self):
        grid = Grid(5, 5)
        for i in range(5):
            a = grid.move_left()
            if self.assertFalse(a):
                self.logger.info("The robot leaves the zone")
                break


class Test_move_right(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger()

    def test_move_right(self):
        grid = Grid(5, 5)
        for i in range(5):
            a = grid.move_left()
            if self.assertFalse(a):
                self.logger.info("The robot leaves the zone")
                break

class Test_grid(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger()

    def test_grid(self):
        grid = Grid(50, 50)
        if self.assertTrue(grid.nb_lines > 20 or grid.nb_columns > 20):
            self.logger.info("The grid cannot have more than 50 lines or 50 columns")