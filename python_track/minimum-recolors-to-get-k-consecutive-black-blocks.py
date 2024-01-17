class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        right = k
        n = len(blocks)

        subs = blocks[:k]
        recolor = 0
        bCounter = 0
        for i in subs:
            if i == "B":
                bCounter +=1
        recolor = k - bCounter
        if recolor == 0:
            return 0

        while right < n :
            if blocks[right]  == "B":
                bCounter += 1

            if blocks[left] == "B" :
                bCounter -=1

            right +=1
            left +=1
            recolor = min(recolor , k - bCounter ) 

        return recolor      




