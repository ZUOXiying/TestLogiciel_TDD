"""Test Logiciel TDD"""
import unittest
import funcs

class TestFuncs(unittest.TestCase):
    """test functions"""
    def test_geometrique(self):
        """test si c’est une suite géométrique"""
        self.assertTrue(funcs.si_geometrique([1,2,4,8,16]))
        self.assertTrue(funcs.si_geometrique([1,1,1,1,1]))
        self.assertTrue(funcs.si_geometrique([-1,1,-1,1,-1]))
        self.assertTrue(funcs.si_geometrique([16,8,4,2,1]))

        self.assertFalse(funcs.si_geometrique([1,2,3,4,5]))
        self.assertFalse(funcs.si_geometrique([2,4,6,8,10]))
        self.assertFalse(funcs.si_geometrique([1,-1,1,-1,-1]))
        self.assertFalse(funcs.si_geometrique([0,0,0,0,0]))

    def test_arithmetique(self):
        """test si c’est une suite arithmétique"""
        self.assertTrue(funcs.si_arithmetique([1,2,3,4,5]))
        self.assertTrue(funcs.si_arithmetique([1,1,1,1,1]))
        self.assertTrue(funcs.si_arithmetique([-1,1,3,5,7]))
        self.assertTrue(funcs.si_arithmetique([16,12,8,4,0]))

        self.assertFalse(funcs.si_arithmetique([1,4,9,16,25]))
        self.assertFalse(funcs.si_arithmetique([-1,1,-1,1,-1]))
        self.assertFalse(funcs.si_arithmetique([2,4,6,8,11]))

    def test_geometrique_plus(self):
        """test si la suite est géométrique et renvoie la liste des n éléments suivant"""
        self.assertEqual(funcs.geometrique_plus(1, [1,2,4,8,16]), [True, [32]])
        self.assertEqual(funcs.geometrique_plus(2, [-1,1,-1,1,-1]), [True, [1,-1]])
        self.assertEqual(funcs.geometrique_plus(3, [16,8,4,2,1]), [True, [0.5,0.25,0.125]])
        self.assertEqual(funcs.geometrique_plus(0, [1,2,4,8,16]), [True, []])
        self.assertEqual(funcs.geometrique_plus(1, [1,2,3,4,5]), False)
        self.assertEqual(funcs.geometrique_plus(0, [2,4,6,8,10]), False)
        self.assertEqual(funcs.geometrique_plus(2, [0,1,0,1,0]), False)

    def test_arithmetique_plus(self):
        """test si la suite est arithmétique et renvoie la liste des n éléments suivant"""
        self.assertEqual(funcs.arithmetique_plus(3, [1,2,3,4,5]), [True, [6,7,8]])
        self.assertEqual(funcs.arithmetique_plus(2, [1,1,1,1,1]), [True, [1,1]])
        self.assertEqual(funcs.arithmetique_plus(3, [-1,1,3,5,7]), [True, [9,11,13]])
        self.assertEqual(funcs.arithmetique_plus(0, [16,12,8,4,0]), [True, []])
        self.assertEqual(funcs.arithmetique_plus(1, [1,4,9,16,25]), False)
        self.assertEqual(funcs.arithmetique_plus(0, [-1,1,-1,1,-1]), False)
        self.assertEqual(funcs.arithmetique_plus(2, [2,4,6,8,11]), False)

    def test_unit_valid(self):
        """test si les données de la grille 3*3 sont en conflit"""
        sudoku1 = [["1","2","3",".","7",".",".",".","."],
  					["4","8","6","1","4","9",".",".","."],
  					["9","5","7",".",".",".",".",".","."],
 					["3",".",".",".","5",".","4",".","3"],
  					["4",".",".",".",".","3",".",".","1"],
					["7",".",".",".","2",".",".",".","6"],
					[".","9",".",".",".",".",".","7","."],
					[".",".",".","2",".","9",".",".","."],
					[".",".",".",".",".",".",".","5","8"]
		]
        self.assertTrue(funcs.unit_valid(sudoku1))
        sudoku2 = [["1","2","3",".","7",".",".",".","."],
  					["4","8","6","1","4","9",".",".","."],
  					["7","5","7",".",".",".",".",".","."],
 					["3",".",".",".","5",".","4",".","3"],
  					["4",".",".",".",".","3",".",".","1"],
					["7",".",".",".","2",".",".",".","6"],
					[".","9",".",".",".",".",".","7","."],
					[".",".",".","2",".","9",".",".","."],
					[".",".",".",".",".",".",".","5","8"]
		]
        self.assertFalse(funcs.unit_valid(sudoku2))

    def test_colonne_valid(self):
        """Déterminer si chaque colonne de données est en conflit"""
        sudoku1 = [["1","2","3",".","7",".",".",".","."],
  					["4","8","6","1","4","9",".",".","."],
  					["9","5","7",".",".",".",".",".","."],
 					["3",".",".",".","5",".","4",".","3"],
  					[".",".",".",".",".","3",".",".","1"],
					["7",".",".",".","2",".",".",".","6"],
					[".","9",".",".",".",".",".","7","."],
					[".",".",".","2",".",".",".",".","."],
					[".",".",".",".",".",".",".","5","8"]
		]
        self.assertTrue(funcs.colonne_valid(sudoku1))
        sudoku2 = [["1","2","3",".","7",".",".",".","."],
  					["4","8","6","1","4","9",".",".","."],
  					["7","5","7",".",".",".",".",".","."],
 					["3",".",".",".","5",".","4",".","3"],
  					["4",".",".",".",".","3",".",".","1"],
					["7",".",".",".","2",".",".",".","6"],
					[".","9",".",".",".",".",".","7","."],
					[".",".",".","2",".","9",".",".","."],
					[".",".",".",".",".",".",".","5","8"]
		]
        self.assertFalse(funcs.colonne_valid(sudoku2))

    def test_ligne_valid(self):
        """Déterminer si chaque ligne de données est en conflit"""
        sudoku1 = [["1","2","3",".","7",".",".",".","."],
  					["4","8","6","1","3","9",".",".","."],
  					["9","5","7",".",".",".",".",".","."],
 					["6",".",".",".","5",".","4",".","3"],
  					[".",".",".",".",".","3",".",".","1"],
					["7",".",".",".","2",".",".",".","6"],
					[".","9",".",".",".",".",".","7","."],
					[".",".",".","2",".",".",".",".","."],
					[".",".",".",".",".",".",".","5","8"]
		]
        self.assertTrue(funcs.ligne_valid(sudoku1))
        sudoku2 = [["1","2","3",".","7",".",".",".","."],
  					["4","8","6","1","4","9",".",".","."],
  					["7","5","7",".",".",".",".",".","."],
 					["3",".",".",".","5",".","4",".","3"],
  					["4",".",".",".",".","3",".",".","1"],
					["7",".",".",".","2",".",".",".","6"],
					[".","9",".",".",".",".",".","7","."],
					[".",".",".","2",".","9",".",".","."],
					[".",".",".",".",".",".",".","5","8"]
		]
        self.assertFalse(funcs.ligne_valid(sudoku2))

    def test_sudoku_valid(self):
        """Déterminer si Sudoku est valide"""
        sudoku1 = [["3","9","6","7","1","2","8","5","4"],
  					["4","7","8","6","5","9","3","1","2"],
  					["1","5","2","3","8","4","9","7","6"],
 					["5","8","1","2","6","7","4","3","9"],
  					["7","2","3","9","4","8","1","6","5"],
					["6","4","9","5","3","1","7","2","8"],
					["2","6","7","8","9","3","5","4","1"],
					["8","3","4","1","2","5","6","9","7"],
					["9","1","5","4","7","6","2","8","3"]
		]
        self.assertTrue(funcs.sudoku_valid(sudoku1))
        sudoku2 = [["3","9","6","7","1","2","8","5","4"],
  					["4","7","8","6","5","9","3","1","2"],
  					["1","5","2","3","8","4","9","7","6"],
 					["5","8","1","2","6","7","4","3","9"],
  					["7","2","3","9","4","8","1","6","5"],
					["6","4","9","5","3","1","7","2","8"],
					["2","6","7","8","9","3","5","4","1"],
					["8","3","4","1","2","5","6","9","3"],
					["9","1","5","4","7","6","2","8","7"]
		]
        self.assertFalse(funcs.sudoku_valid(sudoku2))
if __name__ == '__main__':
    unittest.main()
