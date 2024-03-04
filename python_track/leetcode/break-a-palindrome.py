class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        ans = list(palindrome)
        n = len(ans)
        if n == 1:
            return ""
        for i in range(len(ans)):
            if ans[i] != "a":
                ans[i] = "a"
                break
        if ans != ans[::-1]: return "".join(ans)
        ans = list(palindrome)
        for i in range(len(ans)-1 , -1 ,-1 ):
            if ans[i] == "a":
                ans[i] = "b"
                break
        return "".join(ans)        

