class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
            if len(p)>len(s): return []
            hashmap_=defaultdict(int)
            res=[]
            ans_hashmap=defaultdict(int)
            for i in range(len(p)):
                ans_hashmap[p[i]]+=1
                hashmap_[s[i]]+=1
            res.append(0) if hashmap_==ans_hashmap else []
            l=0
            for r in range(len(p), len(s)):
                hashmap_[s[r]]+=1
                hashmap_[s[l]]-=1
                if hashmap_[s[l]]==0:
                    hashmap_.pop(s[l])
                l+=1
                if hashmap_==ans_hashmap:
                    res.append(l)
            return res