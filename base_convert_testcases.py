import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")
    def test_base16_1(self):   
        self.assertEqual(convert(42,16),"2A")
    def test_base16_2(self):
        self.assertEqual(convert(43,16),"2B")
    def test_base16_3(self):
        self.assertEqual(convert(45,16),"2D")
    def test_base16_4(self):
        self.assertEqual(convert(46,16),"2E")
    def test_base16_5(self):
        self.assertEqual(convert(47,16),"2F")
    def test_base16_6(self):
        self.assertEqual(convert(10,16),"A")
    def test_base16_7(self):
        self.assertEqual(convert(11,16),"B")
    def test_base16_8(self):
        self.assertEqual(convert(12,16),"C")
    def test_base16_9(self):
        self.assertEqual(convert(13,16),"D")
    def test_base16_10(self):
        self.assertEqual(convert(14,16),"E")
    def test_base16_11(self):
        self.assertEqual(convert(15,16),"F")

if __name__ == "__main__":
        unittest.main()