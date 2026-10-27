class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = dict()
        for x in range(len(nums)):
            contra = target - nums[x]
            if contra not in ans:
                ans[nums[x]] = x
            else:
                return [ans[contra], x]