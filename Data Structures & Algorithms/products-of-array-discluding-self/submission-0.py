class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        full_product = 1
        suffix = [1] * len(nums)
        for i in range(1, len(nums)):
            suffix[i] = suffix[i-1] * nums[i-1]
            # full_product = full_product * nums[i]
        output = suffix
        print(output)
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i]*full_product
            full_product = full_product * nums[i]
        
        
            # for j in range(len(nums)):
            #     if i !=j:
            #         product = product * nums[j]
            
            # output.append(product)
        
        return output
        