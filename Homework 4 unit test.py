from unittest import TestCase, main
from Homework_week_4 import pin_validation,calculate_new_balance,withdrawal_validation,pin_digits_validation

class MyTestCase(TestCase):

    def test_rightpin_validation(self):
        expected = True
        result = pin_validation(pin_input=1103)
        self.assertEqual(result,expected)

    def test_pin_digits_if_two_digits(self):
        my_input = 11
        with self.assertRaises(ValueError):
            pin_digits_validation(my_input)

    def test_pin_digits_if_five_digits(self):
        my_input = 11000
        with self.assertRaises(ValueError):
            pin_digits_validation(my_input)

    def test_calculate_new_balance(self):
        expected = 80
        result = calculate_new_balance(withdrawal=20)
        self.assertEqual(expected,result)

    def test_withdrawal_validation_error(self):
        my_input = -10
        with self.assertRaises(ValueError):
            withdrawal_validation(my_input)


if __name__ == '__main__':
    main()
