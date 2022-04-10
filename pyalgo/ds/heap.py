class PriorityQueue:
    def __init__(self, arr: list = [], is_min=True):
        self.arr = arr
        self.minmax = min if is_min else max
        self.heapify()

    @staticmethod
    def children(i):
        return (2 * i + 1, 2 * i + 2)

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    @staticmethod
    def is_root(i):
        return i == 0

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.arr)

    def compare(self, i, j):
        if self.minmax(self.arr[i], self.arr[j]) == self.arr[j]:
            return True
        return False

    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def heapify(self):
        for i in range(self.size() // 2 - 1, -1, -1):
            self.move_down(i)

    def move_down(self, i=0):
        while 2 * i + 1 < self.size():
            l, r = PriorityQueue.children(i)
            j = i
            if self.compare(j, l):
                j = l
            if r < self.size() and self.compare(j, r):
                j = r
            if i == j:
                break
            self.swap(i, j)
            i = j

    def move_up(self, i):
        while not PriorityQueue.is_root(i):
            p = PriorityQueue.parent(i)
            if not self.compare(p, i):
                break
            self.swap(p, i)
            i = p

    def push(self, num):
        self.arr.append(num)
        self.move_up(self.size() - 1)

    def pop(self):
        if self.is_empty():
            return None

        root = self.arr[0]

        new_root = self.arr[-1]
        self.arr[0] = new_root
        self.arr.pop()
        if not self.is_empty():
            self.move_down()
        return root


if __name__ == "__main__":

    q = PriorityQueue([], False)

    for i in range(10):
        i = int(input())
        q.push(i)
    print("=============")
    while not q.is_empty():
        print(q.pop(), end=" ")
