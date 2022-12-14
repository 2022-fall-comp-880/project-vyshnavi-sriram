"""Test Layoffs methods."""

import os
import unittest
from unittest import TestCase
from apps.main import read_dataset


class TestLayoffsMostImpactedIndustries(TestCase):
    """Test most_impacted_industries() method."""

    def setUp(self):
        """Create Layoffs objects for the three testing cases."""
        data_dir = os.path.dirname(__file__) + "/../data"
        self.layoffs_empty = read_dataset(f'{data_dir}/layoffs_empty.txt')
        self.layoffs_first10 = read_dataset(f'{data_dir}/layoffs_first_10.txt')
        self.layoffs_last5 = read_dataset(f'{data_dir}/layoffs_last_5.txt')

    def test_most_impacted_industries_empty(self):
        """Test using layoffs_empty.txt."""
        actual_result1 = self.layoffs_empty.most_impacted_industries()
        expected_result1 = {}
        self.assertDictEqual(actual_result1, expected_result1)

    def test_most_impacted_industries_first_10(self):
        """Test using layoffs_first_10.txt."""
        actual_result2 = self.layoffs_first10.most_impacted_industries()
        expected_result2 = {'E-commerce': 1, 'Cryptocurrency': 2, 'AI': 3,
                            'Customer service': 4, 'PropTech': 5,
                            'Video production': 6, 'HR Tech': 7}
        self.assertDictEqual(actual_result2, expected_result2)

    def test_most_impacted_industries_last_5(self):
        """Test using layoffs_last_5.txt."""
        actual_result3 = self.layoffs_last5.most_impacted_industries()
        expected_result3 = {'Transportation': 1, 'AI': 2, 'Fitness': 3,
                            'PropTech': 4, 'FinTech': 5}
        self.assertDictEqual(actual_result3, expected_result3)


if __name__ == '__main__':
    unittest.main()
