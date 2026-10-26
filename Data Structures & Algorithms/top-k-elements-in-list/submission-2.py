class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash_table = {}
        final_list = []

        for i in range(0, len(nums)):
            if nums[i] in hash_table:
                hash_table[nums[i]] = hash_table[nums[i]]+1
            else:
                hash_table[nums[i]] = 1
        
        sorted_table = dict(sorted(hash_table.items(), key= lambda x:x[1], reverse=True))
        # print(sorted_list) 

        for key, value in sorted_table.items():
            if k!=0:
                final_list.append(key)
                k = k-1
        
        return final_list