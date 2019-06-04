import io
import unittest
from unittest import mock
from src.problem_02.problem_02 import person_b
from src.problem_02.problem_02 import print_depth


class DictionaryDepthsTest(unittest.TestCase):

    def setUp(self):
        self.valid_data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "user": person_b,
                }
            }
        }
        self.expected_data = """key1 1
key2 1
key3 2
key4 2
key5 3
user 3
first_name 4
last_name 4
father 4
first_name 5
last_name 5
father 5
"""
        self.invalid_data = ()

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_dict(self, mock_stdout):
        print_depth(self.valid_data)
        self.assertEqual(self.expected_data, mock_stdout.getvalue())

    def test_invalid_dict(self):
        self.assertRaises(TypeError, lambda: print_depth(self.invalid_data))


if __name__ == '__main__':
    unittest.main()
