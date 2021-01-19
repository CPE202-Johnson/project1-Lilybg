import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")
        self.assertEqual(convert(42,16),"2A")
        self.assertEqual(convert(43,16),"2B")
        self.assertEqual(convert(45,16),"2D")
        self.assertEqual(convert(46,16),"2E")
        self.assertEqual(convert(47,16),"2F")

if __name__ == "__main__":
        unittest.main()