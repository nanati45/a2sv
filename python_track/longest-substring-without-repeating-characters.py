class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sCount = defaultdict(int)
        left = 0
        right = 0
        maxLen = 0
        while right < len(s):
            sCount[s[right]] += 1
            while sCount[s[right]] > 1:
                sCount[s[left]] -=1 
                left += 1

            maxLen = max(maxLen, right - left + 1)     
            right += 1
        return maxLen    

