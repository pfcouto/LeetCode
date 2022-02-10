class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        complementMap = dict()

        for i in range(len(nums)):
            complement = target - nums[i]

            if nums[i] in complementMap:
                return [complementMap[nums[i]], i]
            else:
                complementMap[complement] = i


nums = [2, 7, 11, 15]
target = 9

print(Solution().twoSum(nums, target))
