import unittest
from maiin import *
class maiinTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_str(self):
        s = "......In,, a "
        self.assertEqual(s.translate(str.maketrans('', '', string.punctuation)),"In a ")
    def test_index(self):
        s="In a"
        self.assertEqual(s.split()[0],"In")
    if __name__ == '__main__':
        unittest.main()

