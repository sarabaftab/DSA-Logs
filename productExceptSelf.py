# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
# Each product is guaranteed to fit in a 32-bit integer.

# Example 1:
# Input: nums = [1,2,4,6]
# Output: [48,24,12,8]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in reversed(range(n)):
            output[i] *= right_product
            right_product *= nums[i]

        return output
            
            