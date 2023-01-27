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
        self.assertFalse(funcs.si_geometrique([1,1,1,0,1]))

    def test_arithmetique(self):
        """test si c’est une suite arithmétique"""
        self.assertTrue(funcs.si_arithmetique([1,2,3,4,5]))
        self.assertTrue(funcs.si_arithmetique([1,1,1,1,1]))
        self.assertTrue(funcs.si_arithmetique([-1,1,3,5,7]))
        self.assertTrue(funcs.si_arithmetique([16,12,8,4,0]))

        self.assertFalse(funcs.si_arithmetique([1,4,9,16,25]))
        self.assertFalse(funcs.si_arithmetique([-1,1,-1,1,-1]))
        self.assertFalse(funcs.si_arithmetique([2,4,6,8,11]))

if __name__ == '__main__':
    unittest.main()
