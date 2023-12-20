class Solution:
    def isPalindrome(self, x: int) -> bool:
        xx=str(x)
        if xx==xx[::-1]:
            return True
        return False    