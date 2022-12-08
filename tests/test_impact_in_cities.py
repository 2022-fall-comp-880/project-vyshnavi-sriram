"""Test Layoffs methods."""
import os
import unittest
from unittest import TestCase
from apps.main import read_dataset


class LayoffImpactedCity(TestCase):
    """Test most_impact_city() method."""

    def setUp(self):
        """Create Layoffs objects for the three testing cases."""
        data_dir = os.path.dirname(__file__) + "/../data"
        self.layoffs_empty = read_dataset(f'{data_dir}/layoffs_empty.txt')
        self.layoffs_first10 = read_dataset(f'{data_dir}/layoffs_first_10.txt')
        self.layoffs_last5 = read_dataset(f'{data_dir}/layoffs_last_5.txt')

    def test_layoff_impacted_city_empty(self):
        """Test using layoffs_empty.txt."""
        actual_result = self.layoffs_empty.impact_in_cities()
        expected_result = {}
        self.assertDictEqual(actual_result, expected_result)

    def test_layoff_impacted_city_first_10(self):
        """Test using layoffs_first_10.txt."""
        actual_result1 = self.layoffs_first10.impact_in_cities()
        expected_result1 = {'Stamford': '6.12 %', 'San Francisco': '10.47 %',
                            'Seattle': '81.56 %', 'San Mateo': '0.82 %',
                            'Palo Alto': '0.18 %', 'Lehi': '0.16 %',
                            'Cambridge': '0.33 %', 'Santa Clara': '0.37 %'}
        self.assertDictEqual(actual_result1, expected_result1)

    def test_layoff_impacted_city_last_5(self):
        """Test using layoffs_last_5.txt."""
        actual_result2 = self.layoffs_last5.impact_in_cities()
        expected_result2 = {'Minneapolis': '14.21 %', 'New York': '39.85 %',
                            'Los Angeles': '28.17 %',
                            'Santa Monica': '17.77 %'}
        self.assertDictEqual(actual_result2, expected_result2)


if __name__ == '__main__':
    unittest.main()
