class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        ans = 0
        odds = []
        for i in c :
            if c[i] % 2 == 0:
               ans += c[i]
            else:
                odds.append(c[i])
        ans += sum(odds) - (len(odds) - 1) if odds else 0
        return ans