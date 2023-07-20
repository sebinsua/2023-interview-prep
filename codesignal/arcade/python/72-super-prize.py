class Prizes(object):
    def __init__(self, purchases, n, d):
        self.i = 0
        self.purchases = purchases
        self.n = n
        self.d = d
        
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            if self.i < len(self.purchases):
                current_index = self.i + 1
                if current_index % self.n == 0 and self.purchases[self.i]  % self.d == 0:
                    self.i += 1
                    return current_index
                else:
                    self.i += 1
            else:
                raise StopIteration


def solution(purchases, n, d):
    return list(Prizes(purchases, n, d))
