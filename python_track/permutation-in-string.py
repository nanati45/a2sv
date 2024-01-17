class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)
        left = 0
        right = k

        counter = defaultdict(int)
        sCounter = Counter(s1)
        for i in s2[:k]:
            counter[i] +=1
        if counter == sCounter :
            return True

        while right < n:
            counter[s2[right]] +=1
            counter[s2[left]] -=1
            if counter[s2[left]] == 0:
                counter.pop(s2[left])

            if counter == sCounter :
                return True

            right +=1
            left +=1    

        return False        


            