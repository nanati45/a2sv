class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter=Counter(arr1)
        ans=[]

        for i in arr2:
            for j in range(counter[i]):
                ans.append(i)
            del counter[i]

        for i in sorted(counter):
            for j in range(counter[i]):
                ans.append(i) 
                                   
        return ans         
