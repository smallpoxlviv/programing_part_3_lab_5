import unittest
from main import *


class Test(unittest.TestCase):

	def test_input_data(self):
		haystack, needle, delimiter = input_data('io/test/test_haystack.in',
		 				'io/test/test_needle.in', 'io/test/test_delimiter.in')
		self.assertEqual('gsagsagsagsagsagsagsagoog', haystack)
		self.assertEqual('gsago', needle)
		self.assertEqual('@', delimiter)

	def test_output_data(self):
		result = 15
		file_path = 'io/test/test.out'
		output_data(file_path, result)
		with open(file_path, 'r') as file:
			assert_result = file.readline()
		self.assertEqual(assert_result, str(result))

	def test_prefix(self):
		result = prefix('aabaabaaaabaabaaabcca')
		self.assertEqual(result, [0,1,0,1,2,3,4,5,2,2,3,4,5,6,7,8,9,3,0,0,1])

	def test_delimiter_in_strings(self):
		result = delimiter_in_strings('abbaabaaaabaabaaab', 'aabaa', 'a')
		self.assertEqual(result, True)
		result = delimiter_in_strings('abbaabaaaabaabaaab', 'aabaa', '@')
		self.assertEqual(result, False)

	def test_main(self):
		result = main('abbaabaaaabaabaaab', 'aabaa', '@')
		self.assertEqual(result, 3)

	def test_main_negative(self):
		result = main('abbaabaaaabaabaaab', 'aafaa', '@')
		self.assertEqual(result, -1)

	def test_main_empty_needle(self):
		result = main('abbaabaaaabaabaaab', '', '@')
		self.assertEqual(result, -1)

	def test_main_empty_haystack(self):
		result = main('', 'aabaa', '@')
		self.assertEqual(result, -1)

	def test_main_needle_longer_than_haystack(self):
		result = main('aba', 'aabaa', '@')
		self.assertEqual(result, -1)



if __name__ == "__main__":
	unittest.main()