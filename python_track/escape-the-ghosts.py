class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        ghosts_move=[]
        for i in range(len(ghosts)):
            m=abs(ghosts[i][0]-target[0])
            n=abs(ghosts[i][1]-target[1])
            ghosts_move.append(m+n)
        my_move=abs(target[0])+abs(target[1]) 
        g=min(ghosts_move)
        if my_move<g:
            return True
        return False       