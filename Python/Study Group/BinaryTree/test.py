import unittest
import defs

class Unittest(unittest.TestCase):
    def test_add(self):
        s=defs.Node(6)
        s.add(7)
        self.assertEqual(2,s.height(s))
    def test_height(self):
        s=defs.Node(8)
        s.add(9)
        self.assertEqual(2, s.height(s))
    def test_display(self):
        s = defs.Node(6)
        s.add(7)
        self.assertEqual(2, s.height(s))
if __name__ == '__main__':
    unittest.main()