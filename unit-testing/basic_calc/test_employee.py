import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

  def test_email(self):
    employee_1 = Employee('Sam', 'Wong', 90000)
    employee_2 = Employee('Mom', 'Dad', 95000)
    
    self.assertEqual(employee_1.email, 'Sam.Wong@email.com')
    self.assertEqual(employee_2.email, 'Mom.Dad@email.com')

    employee_1.first = 'Xavier'
    employee_2.first = 'Dad'

    self.assertEqual(employee_1.email, 'Xavier.Wong@email.com')
    self.assertEqual(employee_2.email, 'Dad.Dad@email.com')

  def test_fullname(self):
    employee_1 = Employee('Sam', 'Wong', 90000)
    employee_2 = Employee('Mom', 'Dad', 95000)

    self.assertEqual(employee_1.fullname, 'Sam Wong')
    self.assertEqual(employee_2.fullname, 'Mom Dad')

    employee_1.first = 'Xavier'
    employee_2.first = 'Dad'

    self.assertEqual(employee_1.fullname, 'Xavier Wong')
    self.assertEqual(employee_2.fullname, 'Dad Dad')
     
  def test_apply_raise(self):
    employee_1 = Employee('Sam', 'Wong', 90000)
    employee_2 = Employee('Mom', 'Dad', 95000)

    employee_1.apply_raise()
    employee_2.apply_raise()

    self.assertEqual(employee_1.pay, 94500)
    self.assertEqual(employee_2.pay, 99750)

if __name__ == '__main__':
    unittest.main()