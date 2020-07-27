import unittest
import defs

class Unittest(unittest.TestCase):
    def test_b_serach(self):
        s=defs.BinarySearch()
        lis=[1,2,3]
        val=2
        self.assertNotEqual(-1,s.b_search(lis, 0, len(lis) - 1, val))

if __name__ == '__main__':
    unittest.main()