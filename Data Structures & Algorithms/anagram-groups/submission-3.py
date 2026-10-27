class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictnums = defaultdict(list)
        for x in strs:
            nums = [0] * 26
            for y in range(len(x)):
                nums[ord('a') - ord(x[y])] += 1
            dictnums[tuple(nums)].append(x)
        return list(dictnums.values())