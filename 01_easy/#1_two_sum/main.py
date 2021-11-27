'''
Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time
complexity?
'''
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            if num not in range(-109, 110):
                return None
        if (target in range(-109, 110)) and (len(nums) in range(2, 105)):
            for idx1, num1 in enumerate(nums):
                diff = target - num1
                num_rest = nums[idx1+1:]
                if diff in num_rest:
                    for idx2, num2 in enumerate(num_rest):
                        if num2 == diff:
                            return [idx1, idx1+idx2+1]
        else:
            return None
