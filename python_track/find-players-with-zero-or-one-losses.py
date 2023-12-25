from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners=[]
        losers=[]
        for i in matches:
            winners.append(i[0])
            losers.append(i[1])
        l=Counter(losers)
        res=[]
        not_loser=list(set(winners)-set(losers))
        res.append(sorted(not_loser))
        lose_once=[]  
        for i,k in l.items():
            if k ==1:
                lose_once.append(i)
        res.append(sorted(lose_once))        
        return res