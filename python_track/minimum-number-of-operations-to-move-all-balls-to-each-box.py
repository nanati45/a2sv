class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans=[]
        list_ = []
        leng = len(boxes)
        for i in range(leng):
            if boxes[i]=="1":
                list_.append(i)

        for box in range(leng):
            sum_=0
            for s in range(len(list_)):
                sum_+=abs(list_[s]-box)
            ans.append(sum_)
        return ans    