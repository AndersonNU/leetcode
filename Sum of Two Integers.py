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
                # Operator copies a bit to the result if it exists in both operands
                # 3 is 011; 6 is 110; So 3 & 6 is 010, which is 2
                carry = a & b
                # It copies the bit if it is set in one operand but not both.
                # so a ^ b = 101, which is 5
                a = a ^ b
                # The left operands value is moved left by the number of bits specified by the right operand.
                b = carry << 1
        return a

object = Solution()
print(object.getSum(101,5))
