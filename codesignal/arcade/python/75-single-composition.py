def compose(f, g):
    return lambda x: f(g(x))

def solution(f, g, x):
    return compose(eval(f), eval(g))(x)
