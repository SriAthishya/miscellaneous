import unittest
import defs

class Unittest(unittest.TestCase):
    def test_init(self):
        s=defs.Queue()
        self.assertEqual([],s.display())
    def test_enqueue(self):
        value=7
        s=defs.Queue()
        s.enqueue(value)
        self.assertEqual([7],s.display())
    def test_dequeue(self):
        s=defs.Queue()
        s.enqueue('5')
        s.enqueue('7')
        s.dequeue()
        self.assertEqual(['7'],s.display())
    def test_Front(self):
        s=defs.Queue()
        s.enqueue('9')
        s.enqueue('8')
        self.assertEqual('9',s.front())
    def test_rear(self):
        s=defs.Queue()
        s.enqueue('1')
        s.enqueue('2')
        self.assertEqual('2',s.rear())
    def test_display(self):
        s=defs.Queue()
        s.enqueue('1')
        self.assertEqual(['1'],s.display())

if __name__ == '__main__':
    unittest.main()