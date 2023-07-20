def solution(a, b):
    uniqueSums = {i + j for j in b for i in a if (i * j) % (i + j) == 0}
    return len(uniqueSums)
