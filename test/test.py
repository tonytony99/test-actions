import unittest

from src.add import add

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 3), 4)

if __name__ == '__main__':
    unittest.main()
