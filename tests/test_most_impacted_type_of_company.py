"""Test Layoffs methods."""

import os
import unittest
from unittest import TestCase
from apps.main import read_dataset


class TestLayoffsMostImpactedTypeOfCompany(TestCase):
    """Test most_impacted_type_of_company() method."""

    def test_most_impacted_type_of_company_empty(self):
        """Test using layoffs_empty.txt."""
        data_dir = os.path.dirname(__file__)
        input_file1 = data_dir + "/layoffs_empty.txt"
        layoffs_data1 = read_dataset(input_file1)
        actual_result1 = layoffs_data1.most_impacted_type_of_company()
        expected_result1 = {}
        self.assertDictEqual(actual_result1, expected_result1)

    def test_most_impacted_type_of_company_first_10(self):
        """Test using layoffs_first_10.txt."""
        data_dir = os.path.dirname(__file__)
        input_file2 = data_dir + "/layoffs_first_10.txt"
        layoffs_data2 = read_dataset(input_file2)
        actual_result2 = layoffs_data2.most_impacted_type_of_company()
        expected_result2 = {'Public': {'0 - 20 %': ['Sema4', 'Amazon',
                                                    'Coinbase', 'SoundHound']},
                            'Private': {'0 - 20 %': ['Intercom', 'Reforge'],
                                        '20 - 40 %': ['Veev'], '40 - 60 %':
                                            ['Ocavu', 'Wistia'], '60 - 80 %':
                                            [], '80 - 100 %': ['Wavely']}}
        self.assertDictEqual(actual_result2, expected_result2)


if __name__ == '__main__':
    unittest.main()
