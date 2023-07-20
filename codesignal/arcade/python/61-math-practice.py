import functools

def solution(numbers):
    return functools.reduce(
        lambda acc, pair: acc * pair[0] + pair[1],
        (
            (numbers[i], numbers[i+1] if i+1 < len(numbers) else 0)
            for i in range(0, len(numbers), 2)
        ),
        1
    )
