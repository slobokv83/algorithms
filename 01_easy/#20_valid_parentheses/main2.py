class Solution:
    def isValid(self, s: str) -> bool:
        bracket_order = {"(": [], "[": [], "{": []}
        paired_idx = []
        bracket_pair = {")": "(", "]": "[", "}": "{"}
        for i, bracket in enumerate(s):
            if bracket in bracket_pair.values():
                bracket_order[bracket] += [i]
            else:
                brack = bracket_pair[bracket]
                if bracket_order[brack] == []:
                    return False
                paired_idx.append((bracket_order[brack][-1], i))
                bracket_order[brack].pop()
        tup = ()
        for t in paired_idx:
            tup += t
            if not set(range(t[0], t[1])) <= set(tup):
                return False
        if bracket_order["("] == [] and\
           bracket_order["["] == [] and\
           bracket_order["{"] == []:
            return True
        else:
            return False


# o = Solution()
# print(repr(o.isValid("((()((([[[]]]))))")))
