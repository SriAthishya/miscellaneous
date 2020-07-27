import unittest 
import unittestb
class check_palindrome(unittest.TestCase):
    def test_palin(self):
        str1 = 'malayalam'
        status = unittestb.check_palin(str1)
        self.assertEqual(status,True)
    def test_palin_failure(self):
        str1 = 'mal'
        status = unittestb.check_palin(str1)
        self.assertEqual(status,False)  
    def test_add_success(self):
        n1=10
        n2=12
        num=unittestb.add(n1,n2)
        self.assertEqual(num,22) 
    
   
        
if __name__ == '__main__': 
    unittest.main() 
    
   