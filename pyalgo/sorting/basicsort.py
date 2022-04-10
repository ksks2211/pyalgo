from .common import _get_arr


# Bubble Sort
def bubble_sort(arr, **kwargs):
    arr = _get_arr(arr, kwargs.get("inplace"))

    #  len(arr)-1   >= (i) >= 1
    for i in range(len(arr) - 1, 0, -1):
        swap = False
        # 0<= (j) <=  i-1
        for j in range(i):
            if arr[j] > arr[j + 1]:
                swap = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swap:
            break
    return arr


# Selection Sort
def selection_sort(arr, **kwargs):
    arr = _get_arr(arr, kwargs.get("inplace"))

    #  0 <= (i) <= len(arr)-2
    for i in range(len(arr) - 1):
        sm_idx = i
        # i+1 <= (j) <= len(arr)-1, find smallest
        for j in range(i + 1, len(arr)):
            if arr[sm_idx] > arr[j]:
                sm_idx = j
        # swap
        arr[sm_idx], arr[i] = arr[i], arr[sm_idx]
    return arr


# Insertion Sort
def insertion_sort(arr, **kwargs):
    arr = _get_arr(arr, kwargs.get("inplace"))

    for i in range(1, len(arr)):
        # 추가될 값
        target = arr[i]

        # 추가될 값이 들어갈 위치 찾기
        k = i
        while k > 0 and arr[k - 1] > target:
            arr[k] = arr[k - 1]
            k -= 1
        arr[k] = target
    return arr


if __name__ == "__main__":

    from ..common import random_integers, is_sorted

    arr = list(random_integers(20, 0, 200))

    bubble_sort(arr, inplace=True)

    assert is_sorted(arr)
    print(arr)
