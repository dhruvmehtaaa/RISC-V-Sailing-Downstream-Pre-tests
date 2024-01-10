import unittest
from list_processor import process_list

class TestProcessList(unittest.TestCase):
    def test_simple_case(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        result = process_list(input_list)
        self.assertEqual(result, [1, 5, 7, 11, 13, 17, 19], "Failed for a simple case.")

    def test_empty_list(self):
        input_list = []
        result = process_list(input_list)
        self.assertEqual(result, [], "Failed for an empty input list.")

    def test_invalid_length(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        result = process_list(input_list)
        self.assertIsNone(result, "Failed for invalid input length.")

    def test_non_integer_elements(self):
        input_list = [1, 2, 'three', 4, 5, 6, 7, 8 , 9, 10]
        result = process_list(input_list)
        self.assertIsNone(result, "Failed for non-integer elements.")

if __name__ == "__main__":
    unittest.main()
