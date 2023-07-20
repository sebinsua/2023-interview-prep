from itertools import count, takewhile

def solution(start, stop, step):
    gen = takewhile(lambda num: num < stop, count(start, step))
    return list(gen)
