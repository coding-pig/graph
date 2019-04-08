from src import graph
import unittest

GraphNode = graph.GraphNode

class TestGraph(unittest.TestCase):

    # set up a graph as below
    # 1 ----------> 2 -----------> 3
    # ^             |
    # |             |
    # |             |
    # |             +------------> 4
    # |                            |
    # +----------------------------+           
    def setUp(self):
        # set up vertices
        self.n1 = GraphNode(1)
        self.n2 = GraphNode(2)
        self.n3 = GraphNode(3)
        self.n4 = GraphNode(4)
        # set up edges
        self.n4.to(self.n1)
        self.n1.to(self.n2)
        self.n2.to(self.n3)
        self.n2.to(self.n4)

    def tearDown(self):
        pass

    def test_topology(self):
        self.assertIn(self.n2, self.n1._to)
        self.assertIn(self.n3, self.n2._to)
        self.assertIn(self.n4, self.n2._to)
        self.assertIn(self.n1, self.n4._to)

    # test bfs returning expected nodes and in expected order
    def test_bfs(self):
        n1Reachables = self.n1.bfs()
        self.assertLess(n1Reachables.index(self.n2), n1Reachables.index(self.n3))
        self.assertLess(n1Reachables.index(self.n2), n1Reachables.index(self.n4))
        self.assertLess(n1Reachables.index(self.n3), n1Reachables.index(self.n1))

        n2Reachables = self.n2.bfs()
        self.assertLess(n2Reachables.index(self.n3), n2Reachables.index(self.n1))
        self.assertLess(n2Reachables.index(self.n4), n2Reachables.index(self.n1))
        self.assertLess(n2Reachables.index(self.n1), n2Reachables.index(self.n2))

        n3Reachables = self.n3.bfs()
        self.assertSequenceEqual(n3Reachables, [])

        n4Reachables = self.n4.bfs()
        self.assertLess(n4Reachables.index(self.n1), n4Reachables.index(self.n2))
        self.assertLess(n4Reachables.index(self.n2), n4Reachables.index(self.n3))
        self.assertLess(n4Reachables.index(self.n2), n4Reachables.index(self.n4))

    def test_dfs(self):
        n1Reachables = self.n1.dfs()
        self.assertEqual(n1Reachables[0], self.n2)
        self.assertEqual(n1Reachables.index(self.n4)+1, n1Reachables.index(self.n1))


if __name__ == '__main__':
    unittest.main()
