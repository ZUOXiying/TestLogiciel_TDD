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
if __name__ == '__main__':
    unittest.main()
