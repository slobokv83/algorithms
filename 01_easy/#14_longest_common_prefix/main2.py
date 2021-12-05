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
from typing import List, Tuple


class Solution:
    def ckeckList(self, lst: Tuple[str]) -> bool:
        ele = lst[0]
        # Comparing each element with first item
        for item in lst:
            if ele != item:
                return False
        return True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        ls_tup = list(zip(*strs))
        for tup in ls_tup:
            result = self.ckeckList(tup)
            if result is False:
                return prefix
            prefix += tup[0]
        return prefix


o = Solution()
print(repr(o.longestCommonPrefix(["ffflower", "ffflow", "ffflight"])))
