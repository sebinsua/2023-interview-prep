def solution(x, functions):
    return [fn(x) for fn in map(eval, functions)]
