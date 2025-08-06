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

if __name__ == '__main__':
    unittest.main()