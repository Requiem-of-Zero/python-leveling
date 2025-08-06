import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

  @classmethod # working with class itself
  def setUpClass(cls):
    print('setupClass\n')

  @classmethod
  def tearDownClass(cls):
    print('teardownClass')

  def setUp(self): # Allows mock data variables you can use throughout unittest testcase class, working with instances
    print('setUp')
    self.employee_1 = Employee('Sam', 'Wong', 90000)
    self.employee_2 = Employee('Mom', 'Dad', 95000)

  def tearDown(self): # Allows you to delete any files created from this testcase after test is over
    print('tearDown\n')

  def test_email(self):
    print('testEmail')
    self.assertEqual(self.employee_1.email, 'Sam.Wong@email.com')
    self.assertEqual(self.employee_2.email, 'Mom.Dad@email.com')

    self.employee_1.first = 'Xavier'
    self.employee_2.first = 'Dad'

    self.assertEqual(self.employee_1.email, 'Xavier.Wong@email.com')
    self.assertEqual(self.employee_2.email, 'Dad.Dad@email.com')

  def test_fullname(self):
    print('testFullName')
    self.assertEqual(self.employee_1.fullname, 'Sam Wong')
    self.assertEqual(self.employee_2.fullname, 'Mom Dad')

    self.employee_1.first = 'Xavier'
    self.employee_2.first = 'Dad'

    self.assertEqual(self.employee_1.fullname, 'Xavier Wong')
    self.assertEqual(self.employee_2.fullname, 'Dad Dad')
     
  def test_apply_raise(self):
    print('testApplyRaise')
    self.employee_1.apply_raise()
    self.employee_2.apply_raise()

    self.assertEqual(self.employee_1.pay, 94500)
    self.assertEqual(self.employee_2.pay, 99750)

  def test_monthly_schedule(self):
    print('testMonthlySchedule')
    with patch('employee.requests.get') as mocked_get:
      mocked_get.return_value.ok = True # Create a mock get request response ok to be True
      mocked_get.return_value.text = 'Success' # Create a mock get request response text to be 'Success'

      schedule = self.employee_1.monthly_schedule('May')
      mocked_get.assert_called_with('http://company.com/Wong/May')
      self.assertEqual(schedule, 'Success')

      mocked_get.return_value.ok = False

      schedule = self.employee_2.monthly_schedule('June')
      mocked_get.assert_called_with('http://company.com/Dad/June')
      self.assertEqual(schedule, 'Bad Response!')
      

if __name__ == '__main__':
    unittest.main()