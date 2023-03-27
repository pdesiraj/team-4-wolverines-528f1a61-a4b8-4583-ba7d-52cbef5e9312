from unittest import TestCase
from levelup.position import Position


class TestPosition(TestCase):
    def test_init(self):
        testobj = Position(0, 1)
        expected_position = (0, 1)
        self.assertEqual(testobj.coordinates[0], expected_position[0])
        self.assertEqual(testobj.coordinates[1], expected_position[1])

    def test_equal(self):
        testobj1 = Position(0, 1)
        testobj2 = Position(0, 1)
        self.assertEqual(testobj1, testobj2)

    def test_to_str(self):
        testobj = Position(0, 1)
        expected_str_repr = "(0, 1)"
        self.assertEqual(expected_str_repr, str(testobj))

    def test_equals(self):
        testobj = Position(0, 1)
        testobj2 = Position(0, 1)
        self.assertEqual(testobj, testobj2)
