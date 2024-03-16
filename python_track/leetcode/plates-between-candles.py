class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        plates=[]
        ans=[]

        for i in range(len(s)):
            if s[i]=='|':
                plates.append(i)

        print(plates)
        for start,end in queries:
            left=bisect_left(plates,start)
            right=bisect_right(plates,end)-1
            if left>=right:
                ans.append(0)
                continue
            
            no_of_candles=right-left-1
            no_of_plates = (plates[right]-plates[left]-no_of_candles)-1
            ans.append(no_of_plates)

        return ans