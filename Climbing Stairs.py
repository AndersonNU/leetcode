# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # if n > 2:
        #     return self.climbStairs(n-1) + self.climbStairs(n-2)

        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a

n = 4
object = Solution()
print(object.climbStairs(n))

for i in range(-100,100):
    # if 95**i > i ** 100:
    print(i)
