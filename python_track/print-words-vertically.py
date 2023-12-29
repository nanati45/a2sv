class Solution:
    def printVertically(self, s: str) -> List[str]:
        word_list = [i for i in s.split()]  
        ans = []

        max_len = 0
        for i in word_list:
            max_len = max(max_len,len(i))
        
        for i in range(max_len):
            res = []
            for word in word_list:
                if i < len(word):
                    res.append(word[i])
                else:
                    res.append(" ")
            ans.append("".join(res).rstrip()) 
        return ans         



        



        