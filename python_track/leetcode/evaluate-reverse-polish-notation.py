class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        for i in range(len(tokens)):
            if tokens[i] in operators:
                first = stack.pop()
                res = eval(stack.pop() + tokens[i] +  first)
                stack.append(str(int(res)))
            else:
                stack.append(tokens[i]) 
        return int(stack[0])       
