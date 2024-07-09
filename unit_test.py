import unittest
from find_busiest_intersections import find_busiest_intersections

class TestFindBusiestIntersections(unittest.TestCase):

    def test_one_intersection(self):
        self.assertEqual(find_busiest_intersections( {
            "First": 30,
            "Second": 40,
            "Third": 50,
            "Fourth": 30,
            "Fifth": 30
        }), ["Third"])

    def test_many_intersections(self):
        self.assertEqual(find_busiest_intersections( {
            "First": 32,
            "Second": 35,
            "Third": 35,
            "Fourth": 57,
            "Fifth": 57
        }), ["Fourth","Fifth"])
        
    def test_empty_data(self):
        self.assertEqual(find_busiest_intersections({}), [])


if __name__ == '__main__':
    unittest.main()