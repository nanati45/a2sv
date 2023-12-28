class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1=list("qwertyuiop")
        row2=list("asdfghjkl")
        row3=list("zxcvbnm")
        ans=[]

        word_list=[]
        for w in words:
            word=[]
            for j in w:
                word.append(j.lower())
            word_list.append(word)  

        
        for h in range(len(word_list)):
            r1,r2,r3=0,0,0
            for y in word_list[h]:
                if y in row1:
                    r1+=1 
                elif y in row2:
                    r2+=1
                elif y in row3:
                    r3+=1
            max_=max(r1,r2,r3)
            if max_==len(word_list[h]):
                ans.append(words[h])
    
        return ans    