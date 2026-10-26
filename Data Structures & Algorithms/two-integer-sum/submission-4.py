class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_sum = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash_sum:
                return [hash_sum[diff],i]
            hash_sum[nums[i]] = i
        