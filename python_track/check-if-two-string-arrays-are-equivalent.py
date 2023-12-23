class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        ww=""
        ww2=""
        for i in word1:
            ww+=i
        for i in word2:
            ww2+=i
        return ww==ww2