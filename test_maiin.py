import unittest
from maiin import klopp
class kloppTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_klopp(self):
        stroka="//.,,,In"
        self.assertEqual(klopp(stroka),"In")
    def test_index(self):
        stroka="In пп  вва a"
        self.assertEqual(klopp(stroka),"In")
if __name__ == '__main__':
    unittest.main()


