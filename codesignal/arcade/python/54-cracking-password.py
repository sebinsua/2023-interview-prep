from itertools import product

def solution(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return list(
        sorted(map(
            createNumber,
            filter(
                lambda digits: int(createNumber(digits)) % d == 0,
                product(digits, repeat=k)
            )
        ))
    )
