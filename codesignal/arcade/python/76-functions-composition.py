def compose(functions):
    return lambda x: functools.reduce(lambda acc, f: f(acc), list(functions)[::-1], x)

def solution(functions, x):
    return compose(map(eval, functions))(x)
