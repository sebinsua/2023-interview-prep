def solution(nums, k):
    map = dict()
    for i, n in enumerate(nums):
        if n in map and abs(i - map[n]) <= k:
            return True
        map[n] = i

    return False
