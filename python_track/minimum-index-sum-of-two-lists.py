class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans={}
        for i in list1:
            if i in list2:
                a=list1.index(i)+list2.index(i)
                if a in ans:
                    ans[a].append(i)
                else:
                    ans[a]=[i]
        r=min(ans)
        return ans[r]                

        