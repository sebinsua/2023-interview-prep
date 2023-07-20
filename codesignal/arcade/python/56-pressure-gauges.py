def solution(morning, evening):
    return [
        [min(m, e) for (m, e) in zip(morning, evening)],
        [max(m, e) for (m, e) in zip(morning, evening)]
    ]
