import unittest
import defs

class Unittest(unittest.TestCase):
    def test_init(self):
        s=defs.Stack()
        self.assertEqual(0,s.size())
    def test_is_empty(self):
        a=[]
        if a==[]:
            res=True
        else:
            res=False
        s=defs.Stack()
        self.assertEqual(res,s.is_empty())
    def test_push(self):
        value=7
        s=defs.Stack()
        s.push(value)
        self.assertEqual(1,s.size())
    def test_pop(self):
        s=defs.Stack()
        s.push('5')
        s.push('7')
        s.pop()
        self.assertEqual(['5'],s.display())
    def test_top(self):
        s=defs.Stack()
        s.push('9')
        s.push('8')
        s.top()
        self.assertEqual('8',s.top())
    def test_size(self):
        s=defs.Stack()
        s.push('1')
        self.assertEqual(1,s.size())
    def test_display(self):
        s=defs.Stack()
        s.push('1')
        self.assertEqual(['1'],s.display())

if __name__ == '__main__':
    unittest.main()