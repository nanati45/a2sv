class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        set_= set(fronts).union(set(backs))

        for i in range(len(backs)):
            if backs[i]==fronts[i]:
                set_.discard(backs[i])
        
        return min(list(set_)) if set_ else 0     