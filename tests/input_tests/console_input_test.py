import unittest
from app.io.input import console_input
from unittest.mock import patch

class TestConsoleInput(unittest.TestCase):

    def test_console_input_hello(self):
        user_input = 'hello'
        self.assertEqual(console_input('Enter hello: '), user_input)

    def test_console_input_multiple_inputs(self):
        expected_input = '1'
        self.assertEqual(console_input('Enter 1: '), expected_input)

    @patch('builtins.input', side_effect=[Exception('Test error')])
    def test_console_input_exception(self,mock_input):
        with self.assertRaises(Exception):
            console_input()

if __name__ == '__main__':
    unittest.main()