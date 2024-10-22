from fraction import Fraction
import unittest

class TestInit(unittest.TestCase):
    def test_div_zero(self):
        """Test initialization with zero denominator"""
        with self.assertRaises(ZeroDivisionError, 
            msg="Denominator of zero should raise ZeroDivisionError"):
            Fraction(1, 0)
    
    def test_default(self):
        """Test default constructor (no arguments)"""
        f = Fraction()
        self.assertEqual(str(f), "0/1", 
            msg="Default constructor should create fraction 0/1")
    
    def test_one_arg(self):
        """Test single argument constructor"""
        f = Fraction(5)
        self.assertEqual(str(f), "5/1", 
            msg="Single argument constructor should create fraction n/1")
    
    def test_two_arg(self):
        """Test two argument constructor"""
        f = Fraction(1, 2)
        self.assertEqual(str(f), "1/2", 
            msg="Two argument constructor should create fraction n/d")
    
    def test_float_arg(self):
        """Test float argument raises TypeError"""
        with self.assertRaises(TypeError, 
            msg="Float arguments should raise TypeError"):
            Fraction(2.4)
    
    def test_str_arg(self):
        """Test string argument raises TypeError"""
        with self.assertRaises(TypeError, 
            msg="String arguments should raise TypeError"):
            Fraction("1", "2")
    
    def test_reduced_fraction(self):
        """Test fraction is reduced to lowest terms"""
        f = Fraction(2, 4)
        self.assertEqual(str(f), "1/2", 
            msg="Fraction should be reduced to lowest terms")

class TestStr(unittest.TestCase):
    def setUp(self):
        """Set up common test fractions"""
        self.half = Fraction(1, 2)
        self.whole = Fraction(5, 1)
        self.negative = Fraction(-1, 2)
    
    def test_basic_display(self):
        """Test basic fraction string representation"""
        self.assertEqual(str(self.half), "1/2", 
            msg="Basic fraction should display as 'num/den'")
    
    def test_whole_number(self):
        """Test whole number display"""
        self.assertEqual(str(self.whole), "5", 
            msg="Whole numbers should not display denominator")
    
    def test_negative_display(self):
        """Test negative fraction display"""
        self.assertEqual(str(self.negative), "-1/2", 
            msg="Negative fractions should display as '-num/den'")

class TestFloat(unittest.TestCase):
    def setUp(self):
        """Set up common test fractions"""
        self.half = Fraction(1, 2)
        self.third = Fraction(1, 3)
    
    def test_half_float(self):
        """Test float conversion of 1/2"""
        self.assertEqual(float(self.half), 0.5, 
            msg="Float value of 1/2 should be 0.5")
    
    def test_third_float(self):
        """Test float conversion of 1/3"""
        self.assertAlmostEqual(float(self.third), 0.333333, places=6, 
            msg="Float value of 1/3 should be approximately 0.333333")

class TestAdd(unittest.TestCase):
    def setUp(self):
        """Set up common test fractions"""
        self.f1 = Fraction(1, 2)
        self.f2 = Fraction(1, 3)
    
    def test_add_fractions(self):
        """Test basic fraction addition"""
        result = self.f1 + self.f2
        self.assertEqual(str(result), "5/6", 
            msg="1/2 + 1/3 should equal 5/6")
    
    def test_add_integer(self):
        """Test adding integer to fraction"""
        with self.assertRaises(TypeError, 
            msg="Adding non-Fraction should raise TypeError"):
            self.f1 + 1

class TestSub(unittest.TestCase):
    def setUp(self):
        """Set up common test fractions"""
        self.f1 = Fraction(1, 2)
        self.f2 = Fraction(1, 3)
    
    def test_sub_fractions(self):
        """Test basic fraction subtraction"""
        result = self.f1 - self.f2
        self.assertEqual(str(result), "1/6", 
            msg="1/2 - 1/3 should equal 1/6")
    
    def test_sub_integer(self):
        """Test subtracting integer from fraction"""
        with self.assertRaises(TypeError, 
            msg="Subtracting non-Fraction should raise TypeError"):
            self.f1 - 1

class TestMul(unittest.TestCase):
    def setUp(self):
        """Set up common test fractions"""
        self.f1 = Fraction(1, 2)
        self.f2 = Fraction(2, 3)
    
    def test_mul_fractions(self):
        """Test basic fraction multiplication"""
        result = self.f1 * self.f2
        self.assertEqual(str(result), "1/3", 
            msg="1/2 * 2/3 should equal 1/3")
    
    def test_mul_integer(self):
        """Test multiplying fraction by integer"""
        with self.assertRaises(TypeError, 
            msg="Multiplying by non-Fraction should raise TypeError"):
            self.f1 * 2

class TestTrueDiv(unittest.TestCase):
    def setUp(self):
        """Set up common test fractions"""
        self.f1 = Fraction(1, 2)
        self.f2 = Fraction(1, 4)
        self.zero = Fraction(0, 1)
    
    def test_div_fractions(self):
        """Test basic fraction division"""
        result = self.f1 / self.f2
        self.assertEqual(str(result), "2", 
            msg="1/2 / 1/4 should equal 2")
    
    def test_div_by_zero(self):
        """Test division by zero fraction"""
        with self.assertRaises(ZeroDivisionError, 
            msg="Division by zero fraction should raise ZeroDivisionError"):
            self.f1 / self.zero
    
    def test_div_by_integer(self):
        """Test division by integer"""
        with self.assertRaises(TypeError, 
            msg="Division by non-Fraction should raise TypeError"):
            self.f1 / 2

if __name__ == '__main__':
    unittest.main()
