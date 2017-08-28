# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
#
# Example:
# Given a = 1 and b = 2, return 3.
#
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b is not 0:
                carry = a & b
                a = a ^ b
                b = carry << 1
        return a

object = Solution()
print(object.getSum(101,5))