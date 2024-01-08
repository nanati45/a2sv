class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        r = len(people) - 1
        l = 0
        counter = 0
        while l <= r:
            if(people[r] + people[l] <= limit):
                l += 1
                r -= 1
            else:
                r -= 1
            counter += 1

        return counter