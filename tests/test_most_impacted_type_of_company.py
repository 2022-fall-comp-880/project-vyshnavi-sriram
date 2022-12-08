"""Test Layoffs methods."""

import os
import unittest
from unittest import TestCase
from apps.main import read_dataset


class TestLayoffsMostImpactedTypeOfCompany(TestCase):
    """Test most_impacted_type_of_company() method."""

    def setUp(self):
        """Create Layoffs objects for the three testing cases."""
        data_dir = os.path.dirname(__file__) + "/../data"
        self.layoffs_empty = read_dataset(f'{data_dir}/layoffs_empty.txt')
        self.layoffs_first10 = read_dataset(f'{data_dir}/layoffs_first_10.txt')
        self.layoffs_last5 = read_dataset(f'{data_dir}/layoffs_last_5.txt')

    def test_most_impacted_type_of_company_empty(self):
        """Test using layoffs_empty.txt."""
        actual_result1 = self.layoffs_empty.most_impacted_type_of_company()
        expected_result1 = {}
        self.assertDictEqual(actual_result1, expected_result1)

    def test_most_impacted_type_of_company_first_10(self):
        """Test using layoffs_first_10.txt."""
        actual_result2 = self.layoffs_first10.most_impacted_type_of_company()
        expected_result2 = {'Public': {'0 - 20 %': ['Sema4', 'Amazon',
                                                    'Coinbase', 'SoundHound']},
                            'Private': {'0 - 20 %': ['Intercom', 'Reforge'],
                                        '20 - 40 %': ['Veev'], '40 - 60 %':
                                            ['Ocavu', 'Wistia'], '60 - 80 %':
                                            [], '80 - 100 %': ['Wavely']}}
        self.assertDictEqual(actual_result2, expected_result2)

    def test_most_impacted_type_of_company_last_5(self):
        """Test using layoffs_last_5.txt."""
        actual_result3 = self.layoffs_last5.most_impacted_type_of_company()
        expected_result3 = {'Public': {'0 - 20 %': ['Sezzle', 'Beachbody']},
                            'Private': {'20 - 40 %': ['Hyperscience',
                                                      'Rhino']}}
        self.assertDictEqual(actual_result3, expected_result3)


if __name__ == '__main__':
    unittest.main()
