'''
Given an integer array nums, find the contiguous subarray (containing at least
one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another
solution using the divide and conquer approach, which is more subtle.
'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = []
        negative_nums = [0]
        temp_subarray = []
        previous_subarray = []
        prev_sum = 0
        temp_sum = 0
        flag = False
        for i, num in enumerate(nums):
            # put counter for max_subarray
            # put compare between two max_subarrays
            if num < 0:
                if flag:
                    continue
                if prev_sum > temp_sum:
                    if prev_sum + negative_nums[-1] > 0:
                        # put flag
                        flag = True
                        max_subarray += [negative_nums[-1]] + temp_subarray
                        temp_sum += negative_nums[-1] + prev_sum
                    else:
                        max_subarray = previous_subarray
                else:
                    if prev_sum + negative_nums[-1] > 0:
                        max_subarray += [negative_nums[-1]] + temp_subarray
                        temp_sum += negative_nums[-1] + prev_sum
                    else:
                        print("temp:", temp_subarray)
                        max_subarray = temp_subarray
                negative_nums.append(num)
                previous_subarray = temp_subarray
                prev_sum = temp_sum
                temp_subarray = []
                temp_sum = 0
            else:
                temp_subarray.append(num)
                temp_sum += num
            if i == len(nums) - 1:
                if prev_sum + negative_nums[-1] > 0:
                    # put logic for last
                    pass
        return max_subarray, temp_sum


o = Solution()
ls_subarray = [-5, 2, 1, -4, 1, 2, 3, 4, -5, 2, 1, -3, 6, -1, -2, -3, 4, -5, 2,
               1, -4, 1, 2, 3, 4, -5, 2, 1, -3, 6, -1, -2, -3, 4]
print(repr(o.maxSubArray(ls_subarray)))
