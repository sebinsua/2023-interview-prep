from typing import List, Tuple


def extract_args(stack: List[str]) -> Tuple[int, int]:
    if not stack:
        raise ValueError("The list of tokens was not in reverse polish notation")

    b = stack.pop()
    a = stack.pop()
    return (a, b)


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case "+":
                    a, b = extract_args(stack)
                    stack.append(a + b)
                case "-":
                    a, b = extract_args(stack)
                    stack.append(a - b)
                case "*":
                    a, b = extract_args(stack)
                    stack.append(a * b)
                case "/":
                    a, b = extract_args(stack)
                    stack.append(int(a / b))
                case _:
                    stack.append(int(token))

        return stack[0]
