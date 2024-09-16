"""This module use for statistics.py."""

from unittest import TestCase
from statistics import variance, stdev, average
from math import sqrt


class StatisticsTest(TestCase):
    """Class for test function from statistic.py."""

    def test_variance_typical_values(self):
        """Variance of typical values."""
        self.assertEqual(0.0, variance([10.0, 10.0, 10.0, 10.0, 10.0]))
        self.assertEqual(2.0, variance([1, 2, 3, 4, 5]))
        self.assertEqual(8.0, variance([10, 2, 8, 4, 6]))

    def test_variance_non_integers(self):
        """Variance should work with decimal values."""
        # variance([x,y,z]) == variance([x+d,y+d,z+d]) for any d
        self.assertAlmostEqual(4.0, variance([0.1, 4.1]))
        # variance([0,4,4,8]) == 8
        self.assertAlmostEqual(8.0, variance([0.1, 4.1, 4.1, 8.1]))

    def test_varience(self):
        """Should raise error."""
        with self.assertRaises(ValueError) as context:
            variance([])  # Passing an empty list
        self.assertEqual(str(context.exception), "List must contain at least one value")

    def test_stdev(self):
        """Test stdev function."""
        # standard deviation of a single value should be zero
        self.assertEqual(0.0, stdev([10.0]))
        # simple test
        self.assertEqual(2.0, stdev([1, 5]))
        # variance([0, 0.5, 1, 1.5, 2.0]) is 0.5
        self.assertEqual(sqrt(0.5), stdev([0, 0.5, 1, 1.5, 2]))

    def test_average(self):
        """Test avg function."""
        self.assertEqual(3.0, average([1, 2, 3, 4, 5]))
        self.assertEqual(8.0, average([8, 7, 9]))

    def test_average_raise_error(self):
        """Avg raise error if len == 0."""
        with self.assertRaises(ValueError) as context:
            average([])  # Passing an empty list
        self.assertEqual(str(context.exception), "List must contain at least one value")
