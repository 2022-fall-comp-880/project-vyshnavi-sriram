"""Test Layoffs methods."""
import os
import unittest
from unittest import TestCase
from apps.main import read_dataset


class LayoffImpactedCity(TestCase):
    """Test most_impact_city() method."""

    def layoff_impacted_city_empty(self):
        """Test using layoffs_empty.txt."""
        data_dir = os.path.dirname(__file__)
        input_file = data_dir + "/layoffs_empty.txt"
        layoffs = read_dataset(input_file)
        actual_result = layoffs.impact_in_cities()
        expected_result = {}
        self.assertDictEqual(actual_result, expected_result)

    def layoff_impacted_city_first_10(self):
        """Test using layoffs_first_10.txt."""
        data_dir = os.path.dirname(__file__)
        input_file = data_dir + "/layoffs_first_10.txt"
        layoffs = read_dataset(input_file)
        actual_result = layoffs.impact_in_cities()
        expected_result = {'Stamford': '6.12 %', 'San Francisco': '10.47 %',
                           'Seattle': '81.56 %', 'San Mateo': '0.82 %',
                           'Palo Alto': '0.18 %', 'Lehi': '0.16 %',
                           'Cambridge': '0.33 %', 'Santa Clara': '0.37 %'}
        self.assertDictEqual(actual_result, expected_result)

    def layoff_impacted_city_last_5(self):
        """Test using layoffs_last_5.txt."""
        data_dir = os.path.dirname(__file__)
        input_file = data_dir + "/layoffs_last_5.txt"
        layoffs = read_dataset(input_file)
        actual_result = layoffs.impact_in_cities()
        expected_result = {'Minneapolis': '14.21 %', 'New York': '39.85 %',
                           'Los Angeles': '28.17 %', 'Santa Monica': '17.77 %'}
        self.assertDictEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
