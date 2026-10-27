class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictnums = defaultdict(list)
        for x in strs:
            nums = [0] * 26
            for y in x:
                nums[ord('a') - ord(y)] += 1
            dictnums[tuple(nums)].append(x)
        return list(dictnums.values())