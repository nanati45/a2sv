class Solution:
    def simplifyPath(self, path: str) -> str:
        ls = path.split('/')
        stack = []
        for i in ls:
            if i == '.':
                continue
            if i == '..':
                if stack:
                    stack.pop()
            elif i != "":
                stack.append(i)

        return '/' + '/'.join(stack)