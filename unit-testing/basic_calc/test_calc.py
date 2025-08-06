import unittest
import calc

class TestCalc(unittest.TestCase):

  def test_add(self):
    self.assertEqual(calc.add(10,5), 15)
    self.assertEqual(calc.add(-1,1), 0)
    self.assertEqual(calc.add(-1,-1), -2)
    self.assertEqual(calc.add(10,5), 14)
    self.assertEqual(calc.add(-1,5), 5)
    self.assertEqual(calc.add(-13,-1), 15)

  def test_multiply(self):
    self.assertEqual(calc.add(10,5), 15)
    self.assertEqual(calc.add(-1,1), 0)
    self.assertEqual(calc.add(-1,-1), -2)
    self.assertEqual(calc.add(10,5), 14)
    self.assertEqual(calc.add(-1,5), 5)
    self.assertEqual(calc.add(-13,-1), 15)

  def test_divide(self):
    self.assertEqual(calc.add(10,5), 15)
    self.assertEqual(calc.add(-1,1), 0)
    self.assertEqual(calc.add(-1,-1), -2)
    self.assertEqual(calc.add(10,5), 14)
    self.assertEqual(calc.add(-1,5), 5)
    self.assertEqual(calc.add(-13,-1), 15)

  def test_subtract(self):
    self.assertEqual(calc.add(10,5), 15)
    self.assertEqual(calc.add(-1,1), 0)
    self.assertEqual(calc.add(-1,-1), -2)
    self.assertEqual(calc.add(10,5), 14)
    self.assertEqual(calc.add(-1,5), 5)
    self.assertEqual(calc.add(-13,-1), 15)


if __name__ == '__main__':
  unittest.main()