class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = defaultdict(int)
        for x in nums:
            ans[x] += 1
        sortedlist = sorted(ans.items(), key = lambda item:-item[1])            
        final = []
        for y in range(k):
            final.append(sortedlist[y][0])
        return final

        