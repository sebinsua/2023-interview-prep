def solution(a):
    return [
        a.__setitem__(
            i,
            a[i] if i == 0 else a[i] + a[i-1]
        ) or a[i]
        for i in range(len(a))
    ]
