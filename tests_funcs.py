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
if __name__ == '__main__':
    unittest.main()
