class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        i = 5
        while n//i != 0 :
            result += n//i
            i *= 5
        return result




n = 100
object = Solution()
print(object.trailingZeroes(n))
