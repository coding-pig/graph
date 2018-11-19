from graph import GraphNode
import unittest

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
        n1 = GraphNode(1)
        n2 = GraphNode(2)
        n3 = GraphNode(3)
        n4 = GraphNode(4)
        # set up edges
        n1._from(n4)
        n1._to(n2)
        n2._to(n3)
        n2._to(n4)

        self.graph = [n1, n2, n3, n4]

    def tearDown(self):
        pass

    def test_bfs(self):
        pass

    def test_dfs(self):
        pass


if __name__ == '__main__':
    unittest.main()
