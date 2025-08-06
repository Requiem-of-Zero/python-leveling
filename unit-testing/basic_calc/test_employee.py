import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

  def setUp(self):
    self.employee_1 = Employee('Sam', 'Wong', 90000)
    self.employee_2 = Employee('Mom', 'Dad', 95000)

  def tearDown(self):
    pass

  def test_email(self):
    self.assertEqual(self.employee_1.email, 'Sam.Wong@email.com')
    self.assertEqual(self.employee_2.email, 'Mom.Dad@email.com')

    self.employee_1.first = 'Xavier'
    self.employee_2.first = 'Dad'

    self.assertEqual(self.employee_1.email, 'Xavier.Wong@email.com')
    self.assertEqual(self.employee_2.email, 'Dad.Dad@email.com')

  def test_fullname(self):
    self.assertEqual(self.employee_1.fullname, 'Sam Wong')
    self.assertEqual(self.employee_2.fullname, 'Mom Dad')

    self.employee_1.first = 'Xavier'
    self.employee_2.first = 'Dad'

    self.assertEqual(self.employee_1.fullname, 'Xavier Wong')
    self.assertEqual(self.employee_2.fullname, 'Dad Dad')
     
  def test_apply_raise(self):
    self.employee_1.apply_raise()
    self.employee_2.apply_raise()

    self.assertEqual(self.employee_1.pay, 94500)
    self.assertEqual(self.employee_2.pay, 99750)

if __name__ == '__main__':
    unittest.main()