class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s :
            if i == "]":
                ls = []
                while stack[-1] != "[":
                    ls.append(stack.pop())
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop()+num
                ls = ls * int(num) 
                ls.reverse()
                stack.extend(ls)
            else:
                stack.append(i)
        return "".join(stack)      

               

