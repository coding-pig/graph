class GraphNode:

    def __init__(self, value):
        self.value = value
        self.froms = set() 
        self.tos = set() 

    def _from(self, n):
        self.froms.add(n)

    def _to(self, n):
        self.froms.add(n)
