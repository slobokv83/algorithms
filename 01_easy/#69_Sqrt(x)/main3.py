'''
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and
only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator,
such as pow(x, 0.5) or x ** 0.5.



Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is
truncated, 2 is returned.


Constraints:

0 <= x <= 2^31 - 1
'''

# Babylonian method


class Solution:
    def calc(self, x: int, num: float) -> float:
        print(num)
        return (num + x/num)/2

    def mySqrt(self, x: int) -> int:
        x_len = len(str(x))
        num1 = x
        if x == 2:
            return 1
        if x_len % 2 == 0:
            num = 6 * 10 ** (x_len/2 - 1)
        else:
            num = 2 * 10 ** ((x_len - 1)/2)
        while abs(num1 - num) >= 1:
            num1 = num
            num = self.calc(x, num)
        return int(num)


o = Solution()
print(repr(o.mySqrt(2)))
