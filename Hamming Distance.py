# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, calculate the Hamming distance.
# Note:
# 0 ≤ x, y < 2^31.
# Example:
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ?   ?
#
# The above arrows point to positions where the corresponding bits are different.
#

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # bin is used to convert an integer number to a binary string.
        # print(bin(6))
        return bin(x^y).count('1')

X = Solution()
print(X.hammingDistance(1, 4))
