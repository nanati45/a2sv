class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        c=[]
        for i in words:
            l=[]
            for j in i:
                l.append(order.index(j))
            c.append(l)
        if c==sorted(c):
            return True
        else:
            return False    
        