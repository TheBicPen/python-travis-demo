import powers
import unittest

class test_powers(unittest.TestCase):
    
    def test_same_num_and_base(self):
        self.assertTrue(powers.power_of(6,6))
        
    def test_positive_exponent(self):
        self.assertTrue(powers.power_of(3,27))    
        
    def test_one_base(self):
        self.assertFalse(powers.power_of(1,5))        
    
    def test_zero_base(self):
        self.assertFalse(powers.power_of(0,2))        
        
if __name__ == '__main__':
    unittest.main()