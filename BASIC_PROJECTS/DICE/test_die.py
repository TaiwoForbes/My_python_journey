from die import Die
import unittest

class TestDie(unittest.TestCase):
    
    def testWithNumbergreaterthan(self):
        b = Die(-6)
        self.assertEqual(b.getNumberOfsides(),-6)

    def testNumberOfSIdes(self):
        b = Die(6)
        b.setNumberOfSdies(9)
        self.assertEqual(b.getNumberOfsides(), 9)

    def ifValueisint(self):
        b = Die(5)
        
        self.assertEqual(b.getNumberOfsides(),"str")