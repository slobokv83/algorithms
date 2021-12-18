'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45
'''


class Solution:
    def factorial(self, n):
        fact = 1
        for i in range(1, n+1):
            fact = fact * i
        return fact

    def climbStairs(self, n: int) -> int:
        twoes = int(n / 2)
        sum = 0
        if n % 2 == 0:
            ones = 0
        else:
            ones = 1
        for _ in range(twoes + 1):
            sum += self.factorial(twoes + ones) / (self.factorial(twoes) *
                                                   self.factorial(ones))
            twoes -= 1
            ones += 2

        return int(sum)


o = Solution()
print(repr(o.climbStairs(45)))
