class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.winner_timestamp = defaultdict(int)
        self.counter = defaultdict(int)
        self.prev = {"score" : 0 , "person" : 0}
        self.timestamps = times
        for i in range(len(persons)):
            self.counter[persons[i]] += 1
            if self.prev["score"] <= self.counter[persons[i]]:
                self.prev["score"] = self.counter[persons[i]]
                self.prev["person"] = persons[i]
                self.winner_timestamp[self.timestamps[i]] = persons[i]
            else:
                self.winner_timestamp[times[i]] = self.prev["person"]
    def q(self, t: int) -> int:
        l = 0 
        r = len(self.timestamps) - 1
        while l <= r :
            mid = l + (r - l ) // 2
            if self.timestamps[mid] > t :
                r = mid - 1
            else:
                l = mid + 1
        return self.winner_timestamp[self.timestamps[r]]            


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)