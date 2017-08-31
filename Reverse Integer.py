# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            new_x = -int(str(x)[::-1][:-1])
        else:
            new_x = int(str(x)[::-1])
        return new_x if abs(new_x) < 2147483647 else 0

x = 1000000000000000000000000003
object = Solution()
print(object.reverse(x))
