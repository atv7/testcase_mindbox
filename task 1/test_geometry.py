import unittest
from geometry import Geometry


class TestGeometry(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(Geometry.circle_area(5), 78.5, places=3)

    def test_triangle_area(self):
        self.assertAlmostEqual(Geometry.triangle_area(3, 4, 5), 6.0, places=3)

    def test_is_right_triangle(self):
        self.assertTrue(Geometry.is_right_triangle(3, 4, 5))
        self.assertFalse(Geometry.is_right_triangle(2, 4, 5))

    def test_area(self):
        self.assertAlmostEqual(Geometry.area(5), 78.5, places=3)
        self.assertAlmostEqual(Geometry.area(3, 4, 5), 6.0, places=3)


if __name__ == '__main__':
    unittest.main()
