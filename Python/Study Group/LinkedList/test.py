import unittest
import defs

class Unittest(unittest.TestCase):
    def test_transverse(self):
        s=defs.LinkedList()
        s.ins_at_start('1')
        s.ins_at_end('2')
        self.assertEqual(2,s.size())
    def test_ins_at_start(self):
        s=defs.LinkedList()
        s.ins_at_start('2')
        self.assertEqual(1,s.size())
    def test_ins_at_end(self):
        s=defs.LinkedList()
        s.ins_at_end('1')
        self.assertEqual(1,s.size())
    def test_ins_after_value(self):
        s=defs.LinkedList()
        s.ins_at_start('1')
        s.ins_at_end('3')
        s.ins_after_value('3','2')
        self.assertEqual(3,s.size())
    def test_insert_before_value(self):
        s=defs.LinkedList()
        s.ins_at_start('3')
        s.ins_at_end('1')
        s.insert_before_value('3','2')
        self.assertEqual(3,s.size())
    def test_ins_at_pos(self):
        s=defs.LinkedList()
        s.ins_at_start('1')
        s.ins_at_end('2')
        s.ins_at_pos(2,'3')
        self.assertEqual(3, s.size())
    def test_size(self):
        s=defs.LinkedList()
        s.ins_at_start('6')
        self.assertEqual(1, s.size())
    def test_search(self):
        s=defs.LinkedList()
        s.ins_at_start('3')
        self.assertEqual(True,s.search('3'))
    def test_del_begin(self):
        s = defs.LinkedList()
        s.ins_at_start('1')
        s.ins_at_end('2')
        s.del_begin()
        self.assertEqual(1,s.size())
    def test_del_end(self):
        s = defs.LinkedList()
        s.ins_at_start('1')
        s.ins_at_end('2')
        s.del_end()
        self.assertEqual(1, s.size())
    def test_del_value(self):
        s = defs.LinkedList()
        s.ins_at_start('1')
        s.ins_at_end('2')
        s.del_value('2')
        self.assertEqual(1, s.size())

if __name__ == '__main__':
    unittest.main()