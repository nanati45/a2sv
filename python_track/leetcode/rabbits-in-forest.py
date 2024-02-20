class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        s = 0
        counter = defaultdict(int)
        for i in answers:
            if i== 0:
                s += 1
            else:
                if i in counter:
                    counter[i] -= 1
                    if counter[i] == 0:
                        counter.pop(i)
                else:
                    counter[i] = i
                    s += i + 1  
        return s                
