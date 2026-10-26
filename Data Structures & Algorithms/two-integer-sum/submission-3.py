class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_table = {}
        for i in range(0, len(nums)):
            diff = target - nums[i]
    
            if diff in hash_table:
                return [hash_table[diff], i]
            else:
                hash_table[nums[i]] = i