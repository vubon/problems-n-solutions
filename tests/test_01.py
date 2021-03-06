import io
import unittest
from unittest import mock
from problems.problem_01 import print_depth


class DictionaryDepthsTest(unittest.TestCase):

    def setUp(self):
        self.valid_data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "key6": {
                        "key7": 2
                    }
                }
            }
        }
        self.expected_data = """key1 1
key2 1
key3 2
key4 2
key5 3
key6 3
key7 4
"""
        self.invalid_data = ()

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_data(self, mock_stdout):
        print_depth(self.valid_data)
        self.assertEqual(self.expected_data, mock_stdout.getvalue())

    def test_invalid_data(self):
        self.assertRaises(TypeError, lambda: print_depth(self.invalid_data))

