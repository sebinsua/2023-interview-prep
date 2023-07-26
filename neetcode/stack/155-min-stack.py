class MinStack:
    def __init__(self):
        self._internal_list = []
        self._internal_min_list = []

    def push(self, val: int) -> None:
        self._internal_list.append(val)
        if len(self._internal_min_list) == 0:
            self._internal_min_list.append(val)
        elif val <= self.getMin():
            self._internal_min_list.append(val)

    def pop(self) -> None:
        val = self._internal_list.pop()
        if val == self.getMin():
            self._internal_min_list.pop()
        return val

    def top(self) -> int:
        return self._internal_list[-1]

    def getMin(self) -> int:
        return self._internal_min_list[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
