class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)  #Eliminates duplicates
        max_length = 0
        for item in num_set:
            if (item - 1) not in num_set:
                curr_len = 1

                while item+1 in num_set:
                    curr_len+=1
                    item+=1
                
                max_length = max(curr_len, max_length)
        return max_length

        