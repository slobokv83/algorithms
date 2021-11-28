'''
Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
'''
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) not in range(1, 201):
            return None
        for i, str in enumerate(strs):
            if len(str) not in range(0, 201):
                return None
        prefix = ""
        flag = False
        for id, i in enumerate(strs[0]):
            if len(strs) > 1:
                for j in range(1, len(strs)):
                    if id < len(strs[j]):
                        if i == strs[j][id]:
                            if id == len(strs[j]) - 1:
                                flag = True
                            if j == len(strs) - 1:
                                prefix += strs[j][id]
                        else:
                            return prefix
                if flag:
                    return prefix
            else:
                prefix += i
        return prefix


o = Solution()
print(repr(o.longestCommonPrefix(["flower", "flower", "flower", "flower"])))
