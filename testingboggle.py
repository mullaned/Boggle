import unittest
import boggle

from random import choice
from string import ascii_uppercase

class Test_Boggle(unittest.TestCase):
    def empty_grid_test(self):
        grid = boggle.get_grid()
        self.assertEqual(len(grid), 2)
