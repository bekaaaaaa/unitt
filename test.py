import unittest
from unittest import result

from calc import add, subtract, multiply, divide

class TestAddFunc(unittest.TestCase):
    """
    проверка модуля calc в функцию
    """

    def test_add_integer(self):
        result = add(25, 7)
        self.assertEqual(result, 32)

    def test_add_floats(self):
        result = add(10.5, 3.3)
        self.assertEqual(result, 13.8)

if __name__ == '__main__':
    unittest.main()         

class Test_Sub_integer(unittest.TestCase):
    '''
    проверка модуля calc в функцию
    '''

    def test_sub(self):
        result = subtract(47, 46)
        self.assertEqual(result, 13.8)

if __name__ == '__main__':
    unittest.main()  

class Test_mult(unittest.TestCase):
    """
    проверка модуля calc в функцию
    """

    def test_mult(self):
        result = multiply(5, 5)
        self.assertEqual(result, 25)
    
if __name__ == '__main__':
     unittest.main() 

class Mul(unittest.TestCase):
    """
    проверка модуля calc в функцию
    """
    def test_mul(self):
        result = divide(4.5, 6545)
        self.assertEqual(result, 0.0006875477463712758)

if __name__ == '__main__':
      unittest.main() 

