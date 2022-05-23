class LinkedList:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def add(self, value):
        node = LinkedList(value, self.next)
        self.next = node

    def has(self, value):
        cur = self.next
        while cur:
            if cur.value == value:
                return True
            cur = cur.next
        return False

    def __iter__(self):
        cur = self.next
        while cur:
            yield cur.value
            cur = cur.next


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add(10)
    linked_list.add(20)
    linked_list.add(30)
    linked_list.add(40)

    for val in linked_list:
        print(val)
