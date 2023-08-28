#!/usr/bin/env python3
"""test_utils.py"""
import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """Test case class for the access_nested_map function."""

    @parameterized.expand([
        ({'a': 1}, ['a'], 1),
        ({'a': {'b': 2}}, ['a', 'b'], 2),
        ({'a': {'b': {'c': 3}}}, ['a', 'b', 'c'], 3),
        ({'a': {'b': {'c': {'d': 4}}}}, ['a', 'b', 'c', 'd'], 4),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Test the access_nested_map function with different inputs.

        Args:
            nested_map (dict): The nested map to access.
            path (list): The path to the desired value within the nested map.
            expected_result: The expected result when accessing the nested map.

        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
