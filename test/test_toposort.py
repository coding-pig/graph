from src import toposort
from src import graph
import unittest


GraphNode = graph.GraphNode


class TestTopoSort(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_toposort_1(self):
        a = GraphNode('a')
        b = GraphNode('b')
        b.to(a)
        c = GraphNode('c')
        c.to(a)
        d = GraphNode('e')
        d.to(c)
        e = GraphNode('e')
        e.to(a)
        e.to(b)
        e.to(d)

        self.assertEqual(type(toposort.toposort), type(lambda: 0))
        self.assertEqual(toposort.toposort([a, b, c, d, e]),
                         [[a], [b, c], [d], [e]])

    def test_toposort_2(self):
        a = GraphNode('a')
        b = GraphNode('b')
        b.to(a)

        self.assertSequenceEqual(toposort.toposort([a, b]), [[a], [b]])

    def test_toposort_cycle(self):
        pass


if __name__ == "__main__":
    unittest.main()
