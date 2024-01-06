class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        dist = defaultdict(list)
        for i in points:
            s = i[0]**2 + i[1]**2
            dist[s].append(i)

        sorted_dict = dict(sorted(dist.items(), key=lambda x: x[0]))
        for i in sorted_dict:
            ans.extend(sorted_dict[i])
            
        return ans [:k]    