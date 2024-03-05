class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        window = set()
        c = Counter (s)
        have = 0
        res = []
        l =0
        for i in range(len(s)):
            if s[i] not in window :
                have += 1
            window.add(s[i])
            c[s[i]] -= 1
            if c[s[i]] == 0:
                have -=1 
            if have == 0:
                res.append(i-l +1)
                l = i + 1
                window = set()
        return res
