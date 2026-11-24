import unittest

from rack import pue, rack_heat_btu, rack_power


class RackTests(unittest.TestCase):
    def test_power(self):
        self.assertAlmostEqual(rack_power(20, 450), 9.0)

    def test_heat(self):
        self.assertAlmostEqual(rack_heat_btu(1), 3412)

    def test_pue(self):
        self.assertAlmostEqual(pue(1500, 1000), 1.5)

    def test_negative(self):
        with self.assertRaises(ValueError):
            rack_power(-1, 100)


if __name__ == "__main__":
    unittest.main()
