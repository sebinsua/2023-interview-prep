def solution(male, female):
    return list(zip(*[(m, f) for m, f in zip(male, female) if m != f])) or [[], []]