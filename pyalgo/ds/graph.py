from collections import defaultdict


class AdjacencyMatrix:

    INF = int(1e9)
    # n : number of nodes
    def __init__(self, n, weighted=False):

        self.unconnected = 0 if not weighted else AdjacencyMatrix.INF
        self.graph = [[self.unconnected] * n for _ in range(n)]

    def connect(self, i, j, distance=1):
        self.graph[i][j] = distance

    def disconnect(self, i, j):
        self.graph[i][j] = self.unconnected

    def connected(self, i, j):
        return self.graph[i][j] != self.unconnected

    def distance(self, i, j):
        return self.graph[i][j]

    def graph(self):
        return self.graph


class AdjacencyList:
    def __init__(self, weighted=False):
        self.weighted = weighted
        self.graph = defaultdict(list)

    def connect(self, i, j, distance=1):
        node = j if not self.weighted else (j, distance)
        self.graph[i].append(node)

    def neighbors(self, i):
        return self.graph[i]

    def graph(self):
        return self.graph


if __name__ == "__main__":

    adjmat = AdjacencyMatrix(5)

    adjmat.connect(1, 2)
    adjmat.connect(2, 3)
    adjmat.connect(3, 1)
    adjmat.connect(1, 3)
    adjmat.connect(3, 4)

    assert adjmat.connected(1, 2) is True
    adjmat.disconnect(1, 2)
    assert adjmat.connected(1, 2) is False

    adjlist = AdjacencyList()
    adjlist.connect(1, 2)
    adjlist.connect(1, 3)
    adjlist.connect(2, 3)
    adjlist.connect(3, 1)
    adjlist.connect(3, 4)

    assert 2 in adjlist.neighbors(1)
    assert 3 in adjlist.neighbors(1)
