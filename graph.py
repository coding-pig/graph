class GraphNode:

    def __init__(self, value):
        self._value = value
        self._to = set() 

    # make n a direct destination for self
    def to(self, n):
        self._to.add(n)

    # return list of all reachable nodes from self via bfs
    # nearer nodes appear earlier in returned list
    def bfs(self):
        toOpen, toReturn = [self], [] 
        while len(toOpen) > 0:
            top = toOpen.pop(0)
            for to in top._to:
                if to not in toReturn: # O(N) check. Use a set to make it O(1)
                    toReturn.append(to)
                    if to is not self:
                        toOpen.append(to)

        return toReturn 

    # return set of all reachable nodes from self via dfs
    def dfs(self):
        return set()
