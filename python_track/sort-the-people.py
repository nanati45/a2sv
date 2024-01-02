class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        de=[(heights[i], n) for i,n in enumerate(names) ]
        de.sort()
        print(de)
        ans=[]
        for i in de[::-1]:
            ans.append(i[1])
        return ans