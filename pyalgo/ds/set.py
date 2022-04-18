class BitSet:
    def __init__(self) -> None:
        self.S = 0
        self.MAX = 0

    def clear(self) -> None:
        self.S = 0

    def add(self, el: int) -> None:
        self.S = self.S | (1 << el)
        self.MAX = max(self.MAX, el)

    def remove(self, el: int) -> None:
        self.S = self.S & ~(1 << el)

    def remove_and_reset(self, el: int) -> None:
        self.remove(el)
        if self.MAX == el:
            for i in range(self.MAX, 0, -1):
                if self.has(i):
                    self.MAX = i
                    break

    def toggle(self, el) -> None:
        self.S = self.S ^ (1 << el)

    def has(self, el):
        return 0 != (self.S & (1 << el))

    def elements(self):
        return [i for i in range(1, self.MAX + 1) if self.has(i)]

    def __iter__(self):
        for i in range(1, self.MAX + 1):
            if self.has(i):
                yield i


if __name__ == "__main__":
    s = BitSet()

    s.add(10)
    s.add(1)
    s.add(5)
    s.add(20)

    for el in s:
        print(el)

    print(s.has(10))
