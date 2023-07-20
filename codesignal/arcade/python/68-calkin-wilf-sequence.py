def solution(number):
    def fractions():
        numerator, denominator = 1, 1
        while True:
            yield [numerator, denominator]
            numerator, denominator = (
                denominator,
                2*(numerator // denominator)*denominator + denominator - numerator
            )

    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res
