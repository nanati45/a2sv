class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dire = deque()
        rad = deque()
        offset = len(senate)
        for i in range(len(senate)):
            if senate[i] == "R":
                rad.append(i)
            else:
                dire.append(i) 
        while rad and dire:
            d = dire.popleft()
            r = rad.popleft()
            if d < r :
                dire.append(d + offset)
            else:
                rad.append(r + offset)
        return "Radiant" if rad else "Dire"            