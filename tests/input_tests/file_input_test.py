import unittest
from app.io.input import file_input

class TestFileInput(unittest.TestCase):
    def setUp(self):
        self.test_file_name = 'test_file.txt'
        self.test_file_content = 'Test file content\n'
        with open(f'data/{self.test_file_name}', 'w') as f:
            f.write(self.test_file_content)

    def test_file_input_existing_file(self):
        expected_content = self.test_file_content
        self.assertEqual(file_input(self.test_file_name), expected_content)

    def test_file_input_nonexistent_file(self):
        non_existent_file_name = 'non_existent_file.txt'
        with self.assertRaises(FileNotFoundError):
            file_input(non_existent_file_name)

    def test_file_input_special_characters(self):
        special_characters_file_name = 'special_characters.txt'
        special_characters_content = 'Special characters: !@#$%^&*()_+\n'
        with open(f'data/{special_characters_file_name}', 'w') as f:
            f.write(special_characters_content)
        self.assertEqual(file_input(special_characters_file_name), special_characters_content)

if __name__ == '__main__':
    unittest.main()