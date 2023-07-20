class Counter(object):
    def __init__(self, beta):
        self.value = beta

    def inc(self):
        self.value += 1

    def get(self):
        return self.value


def solution(beta, k, visitors):
    counter = Counter(beta)
    for visitor in visitors:
        if visitor >= k:
            counter.inc()
    return counter.get()
