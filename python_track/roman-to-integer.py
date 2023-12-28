class Solution:
    def romanToInt(self, s: str) -> int:
        dict_={
            "I"  :  1,
            "V" :  5,
            "X"  : 10,
            "L"  : 50,
            "C"  : 100,
            "D"  : 500,
            "M"  : 1000
        }

        stack=[]
        for r in s:
            if not stack:
                stack.append(dict_[r])
            else:
                if stack[-1]>=dict_[r]:
                    stack.append(dict_[r])
                else:
                    stack.append(dict_[r]-stack.pop()) 
                    
        return sum(stack)