"""Archivo que contiene las pruebas unitarias del programa
    """

import unittest

class ArthmeticTestCase(unittest.TestCase):
    def test_sum_check(self):
        ## Declarar las variables
        import arth
        x = 4
        y = 9
        res = 13
        # Ejecucion
        res_sum = arth.sum(x,y)

        # Assert
        self.assertEqual(res, res_sum)