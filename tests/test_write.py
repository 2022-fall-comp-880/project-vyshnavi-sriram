"""Test Layoffs methods."""

import unittest
import os
from unittest import TestCase
from apps.main import read_dataset


class TestPlayerDataWrite(TestCase):
    """Test write() method."""

    def test_write(self):
        """Test checking first row in the Layoff.CSV file."""
        filename = 'layoffs.csv'
        data_dir = os.path.dirname(__file__)
        input_file = data_dir + "/layoffs.txt"
        layoff_data = read_dataset(input_file)
        layoff_data.write(filename)
        with open(filename, 'r') as layoffs_file_obj:
            actual_result = layoffs_file_obj.readline()
            expected_result = 'Sema4,750,16,AI,Stamford,Public\n'
            self.assertEqual(actual_result, expected_result,
                             msg='First line written to file is incorrect')


if __name__ == '__main__':
    unittest.main()
