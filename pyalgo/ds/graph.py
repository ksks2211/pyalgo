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

    def is_connected(self, i, j):
        return self.graph[i][j] != self.unconnected

    def get_distance(self, i, j):
        return self.graph[i][j]


class AdjacencyList:
    def __init__(self, weighted=False):
        self.weighted = weighted
        self.graph = defaultdict(list)

    def connect(self, i, j, distance=1):
        node = j if not self.weighted else (j, distance)
        self.graph[i].append(node)

    def neighbors(self, i):
        return self.graph[i]
