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
    def count(self, tup, el1):
        i = 0
        for t in tup:
            if t == el1:
                i += 1

        return i

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        ls_tup = list(zip(*strs))
        for tup in ls_tup:
            result = self.count(tup, tup[0]) == len(tup)
            if result is False:
                return prefix
            prefix += tup[0]
        return prefix


o = Solution()
print(repr(o.longestCommonPrefix(["flower", "flower", "flower", "flower"])))
