def search_max(possibles, checker):
    start, end = 0, len(possibles) - 1
    while start <= end:
        center = (start + end) // 2
        if checker(possibles[center]):
            if center == start:
                return center
            start = center
        else:
            end = center - 1
    return None


def search_min(possibles, checker):
    start, end = 0, len(possibles) - 1
    while start <= end:
        center = (start + end) // 2
        if checker(possibles[center]):
            if center == start:
                return center
            end = center
        else:
            start = center + 1
    return None
