class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictnums = dict()
        for x in strs:
            nums = [0] * 26
            for y in range(len(x)):
                nums[ord('a') - ord(x[y])] += 1
            if str(nums) not in dictnums:
                dictnums[str(nums)] = [x]
            else:
                dictnums[str(nums)].append(x)
        return list(dictnums.values())