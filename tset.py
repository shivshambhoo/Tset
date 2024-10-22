import unittest

def add(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        # Test case for the add function
        self.assertEqual(add(1, 2), 3)  # Expected outcome is 3
        self.assertEqual(add(-1, 1), 0) # Expected outcome is 0
        self.assertEqual(add(0, 0), 0)  # Expected outcome is 0

    def test_add_negative(self):
        # Another test case with negative numbers
        self.assertEqual(add(-1, -1), -2)  # Expected outcome is -2

if __name__ == '__main__':
    unittest.main()
