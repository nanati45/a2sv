class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        leng = len(skill)//2
        ls1 = skill[:leng]
        ls2 = skill[leng:][::-1]

        ans = 0
        equalizer = ls1[0] + ls2[0]
        for i in range(leng):
            if ls1[i] + ls2[i] == equalizer:
                ans += ls1[i] * ls2[i]
            else:
                return -1   

        return ans    