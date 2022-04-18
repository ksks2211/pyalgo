class DisjointSet:
    def __init__(self, vertices: set) -> None:
        self.parent = {i: i for i in vertices}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px < py:
            self.parent[py] = px
        else:
            self.parent[px] = py
