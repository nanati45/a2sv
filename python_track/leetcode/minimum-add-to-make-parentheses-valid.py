class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for i in s:
            if i == '(' or not stack or (stack and stack[-1] != '('):
                stack.append(i)
            else:
                stack.pop()
            # print(stack)
        return len(stack)