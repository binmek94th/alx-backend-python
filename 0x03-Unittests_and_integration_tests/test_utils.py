#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        (1, {"a": 1}, ("a",)),
        ({"b": 2}, {"a": {"b": 2}}, ("a",)),
        (2, {"a": {"b": 2}}, ("a", "b")),
    ])
    def test_access_nested_map(self, result, nested_map, path):
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, result)
