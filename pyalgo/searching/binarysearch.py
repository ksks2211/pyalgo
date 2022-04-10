from bisect import bisect_left, bisect_right


def _binary_search(arr, target, start, end) -> int:
    if start > end:
        return -1
    center = (start + end) // 2

    if arr[center] == target:
        return center
    elif start == end:
        return -1
    elif arr[center] < target:
        return _binary_search(arr, target, center + 1, end)
    else:
        return _binary_search(arr, target, start, center - 1)


def binary_search_recursive(arr, target) -> int:
    return _binary_search(arr, target, 0, len(arr) - 1)


def binary_search(arr, target) -> int:
    start, end = 0, len(arr) - 1
    while start <= end:
        center = (start + end) // 2
        if arr[center] == target:
            return center
        elif center == start:
            return -1
        elif arr[center] < target:
            start = center + 1
        else:
            end = center - 1
    return -1


def binary_count(arr, target) -> int:
    return bisect_right(arr, target) - bisect_left(arr, target)


if __name__ == "__main__":
    arr = [1, 2, 3, 3, 3, 4, 5, 6]
    print(binary_count(arr, 10))
