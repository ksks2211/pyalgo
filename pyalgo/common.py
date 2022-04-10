import random


def is_sorted(arr):
    cnt = len(arr)
    if cnt < 2:
        return True
    for i in range(1, cnt):
        if arr[i - 1] > arr[i]:
            return False
    return True


def random_integers(cnt, start, end):
    for _ in range(cnt):
        yield random.randint(start, end)


if __name__ == "__main__":

    sorted_list = [1, 2, 3, 4, 5]
    unsorted_list = [1, 6, 2, 8, 3]

    assert is_sorted(sorted_list) is True
    assert is_sorted(unsorted_list) is False

    print(list(random_integers(10, 0, 10)))
