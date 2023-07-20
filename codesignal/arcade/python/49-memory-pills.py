from itertools import dropwhile

def solution(pills):
    gen = dropwhile(lambda s: len(s) % 2 != 0, pills + ["", "", ""])
    next(gen)
    return [next(gen) for _ in range(3)]
