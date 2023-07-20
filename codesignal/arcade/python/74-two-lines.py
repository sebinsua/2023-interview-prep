from functools import partial

def line_y(m, b, x):
    return m * x + b

def solution(line1, line2, l, r):
    line1_y = partial(lambda x: line_y(*line1, x))
    line2_y = partial(lambda x: line_y(*line2, x))
    balance = 0
    for x in range(l, r + 1):
        y1 = line1_y(x)
        y2 = line2_y(x)
        if y1 > y2:
            balance += 1
        elif y1 < y2:
            balance -= 1
    if balance > 0:
        return "first"
    if balance < 0:
        return "second"
    return "any"
