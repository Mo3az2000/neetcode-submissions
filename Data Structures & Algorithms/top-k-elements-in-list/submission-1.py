class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1;
            else:
                d[n] = 1

        sd = sorted(d, key=lambda k: d[k], reverse=True)
        return sd[0:k:1]
        
