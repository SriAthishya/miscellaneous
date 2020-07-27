import unittest
import defs

class Unittest(unittest.TestCase):
    def test_bubble(self):
        s=defs.BubbleSort()
        l1=[8,5,13]
        self.assertEqual(3,len(l1))
if __name__ == '__main__':
    unittest.main()