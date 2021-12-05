'''
Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true


Constraints:

1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
'''


class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s) not in range(1, 10**4 + 1):
        #     return None
        bracket_order = {"(": [], "[": [], "{": []}
        paired_idx = set()
        bracket_pair = {")": "(", "]": "[", "}": "{"}
        for i, bracket in enumerate(s):
            # if bracket not in (list(bracket_pair.keys()) +
            #                    list(bracket_pair.values())):
            #     return None
            if bracket in bracket_pair.values():
                bracket_order[bracket] += [i]
            else:
                brack = bracket_pair[bracket]
                if bracket_order[brack] == []:
                    return False
                paired_idx.add(bracket_order[brack][-1])
                paired_idx.add(i)
                if not set(range(bracket_order[brack][-1], i)) <= paired_idx:
                    return False
                bracket_order[brack].pop()
        if bracket_order["("] == [] and\
           bracket_order["["] == [] and\
           bracket_order["{"] == []:
            return True
        else:
            return False


# o = Solution()
# print(repr(o.isValid("()[]{}.")))
