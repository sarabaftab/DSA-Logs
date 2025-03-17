#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#Example 1:

#Input: nums = [1,2,3,1]

#Output: true

#Explanation:

#The element 1 occurs at the indices 0 and 3.

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
