class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # #Brute force method - O(n^2)
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        
        # Optimized solution using hash table
        hash_table = {}
        for i in range(0, len(nums)):
            if nums[i] in hash_table:
                return True
            hash_table[nums[i]] = 1

        return False

        