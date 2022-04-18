from ..ds import DisjointSet


def has_undirected_cycle(edges, vertices):
    s = DisjointSet(vertices)

    for v, w in edges:
        if s.find(v) == s.find(w):
            return True
        else:
            s.union(v, w)
    return False


if __name__ == "__main__":
    edges = [(1, 2), (2, 3), (3, 4)]
    vertices = {1, 2, 3, 4}
    print(has_undirected_cycle(edges, vertices))
