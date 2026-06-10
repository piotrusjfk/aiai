import main
import unittest

class TestSuma(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(main.suma(10, 10), 20)
        self.assertNotEqual(main.suma(10, 10), 100)

class TestV(unittest.TestCase):
    def test_V(self):
        self.assertEqual(main.V(200, 4), 50)


if __name__ == '__main__':
    unittest.main()