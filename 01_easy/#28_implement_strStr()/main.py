'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question
to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty
string. This is consistent to C's strstr() and Java's indexOf().



Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:

Input: haystack = "", needle = ""
Output: 0


Constraints:

0 <= haystack.length, needle.length <= 5 * 10^4
haystack and needle consist of only lower-case English characters.
'''


class Solution:
    def ret_idx(self, i, haystack, needle):
        len_needle = len(needle)
        j = 0
        for i in range(i, len(haystack)):
            if haystack[i] == needle[j]:
                j += 1
            else:
                return None
            if j == len_needle:
                return i - len_needle + 1

    def strStr(self, haystack: str, needle: str) -> int:
        res = 0
        if needle == "":
            return 0

        for i, hay in enumerate(haystack):

            if hay == needle[0]:
                res = self.ret_idx(i, haystack, needle)
                if res is not None:
                    return res
                # flag = True
            # if flag:
            #     if hay == needle[j]:
            #         j += 1
            #     else:
            #         j = 0
            #         flag = False
            #     if j == len_needle:
            #         return i - len_needle + 1
        return -1


o = Solution()
print(repr(o.strStr("aabaabbbaabbbbabaaab", "abaa")))
