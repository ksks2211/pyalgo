from .common import _get_arr
from collections import Counter


def _quick_sort(arr, start, end):
    if start >= end:
        return

    pivot = arr[start]
    l, r = start + 1, end

    while True:
        #  start+1 <= l <= end+1
        while l <= end and arr[l] <= pivot:
            l += 1
        # start <= r <= end
        while r > start and arr[r] >= pivot:
            r -= 1

        if l < r:
            arr[l], arr[r] = arr[r], arr[l]
        else:  # Change Pivot & Break
            arr[r], arr[start] = arr[start], arr[r]
            break
    _quick_sort(arr, r + 1, end)
    _quick_sort(arr, start, r - 1)


def quick_sort(arr, **kwargs):
    arr = _get_arr(arr, kwargs.get("inplace"))
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


def _move_down(arr, i, n):
    while 2 * i + 1 < n:  # while left-child exists
        l, r, biggest_idx = 2 * i + 1, 2 * i + 2, i
        if arr[l] > arr[biggest_idx]:
            biggest_idx = l
        if r < n and arr[r] > arr[biggest_idx]:
            biggest_idx = r
        if i == biggest_idx:
            break  # heapify completed
        arr[i], arr[biggest_idx] = arr[biggest_idx], arr[i]
        i = biggest_idx


def heap_sort(arr, **kwargs):
    n = len(arr)
    arr = _get_arr(arr, kwargs.get("inplace"))

    # heapify (max-heap)
    for i in range(n // 2 - 1, -1, -1):
        _move_down(arr, i, n)

    for m in range(n - 1, 0, -1):
        arr[m], arr[0] = arr[0], arr[m]
        _move_down(arr, 0, m)

    return arr


def count_sort(arr):
    start, end = min(arr), max(arr) + 1
    cnt = Counter(arr)

    res = []
    for el in range(start, end):
        if cnt[el]:
            res.extend([el] * cnt[el])
    return res


def _merge(arr, left, right):

    i, j = len(left), len(right)
    x, y, z = 0, 0, 0

    while x < i and y < j:
        if left[x] < right[y]:
            arr[z] = left[x]
            x += 1
        else:
            arr[z] = right[y]
            y += 1
        z += 1
    while x < i:
        arr[z] = left[x]
        x += 1
        z += 1
    while y < j:
        arr[z] = right[y]
        y += 1
        z += 1


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    _merge(arr, left, right)
    return arr


if __name__ == "__main__":
    from ..common import random_integers, is_sorted

    arr = list(random_integers(20, 0, 20))
    print("Before Sorting : ", arr)
    arr = merge_sort(arr)
    assert is_sorted(arr)
    print("After Sorting : ", arr)
