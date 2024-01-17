class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        cVowels = 0
        vowels =["a", "e" , "i", "o", "u"]
            
        subs = s[:k]
        for i in subs :
            if i in vowels:
                cVowels += 1

        if cVowels == k:
            return k

        mx = cVowels
        n = len(s)
        ptr = k
        left = 0
        while ptr < n:
            if s[left] in vowels:
                cVowels -=1

            if s[ptr] in vowels:
                cVowels +=1

            ptr +=1 
            left +=1 
            mx = max(cVowels, mx) 
            
        return mx
