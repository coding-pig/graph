from src import toposort
import unittest


class TestTopoSort(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_toposort(self):
        self.assertEqual(type(toposort.toposort), type(lambda: 0))
        self.assertRaises(Exception, toposort.toposort)


if __name__ == "__main__":
    unittest.main()
