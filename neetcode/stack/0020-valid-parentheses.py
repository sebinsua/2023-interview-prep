class Solution:
    def isValid(self, s: str) -> bool:
        open_parens = {"{": "}", "[": "]", "(": ")"}
        close_parens = {
            close_paren: open_paren for (open_paren, close_paren) in open_parens.items()
        }

        stack = []
        for c in s:
            if c in open_parens:
                stack.append(c)
                continue
            if c in close_parens:
                if len(stack) > 0 and close_parens[c] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
