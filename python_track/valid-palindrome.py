class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphanumeric = []
        for char in s:
            if char.isalnum():
                alphanumeric.append(char)
        return alphanumeric== alphanumeric[::-1]