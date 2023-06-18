# 217. Contains Duplicate
# Easy
# Companies
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109


# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#        for i in range (1,5):
#            if(int(nums.count(i))>=2):
#                return True
#            else:
#                return False            

# sol = Solution()
# a = sol.containsDuplicate([1,2,3,1])
# print(a)

#This works well but for distinct it doesn't

class Solution:
        def containsDuplicate(self, nums: list[int]) -> bool:
            hash_Set = set()
            for i in nums:
                if i in hash_Set:
                    return True
                else:
                    hash_Set.add(i)