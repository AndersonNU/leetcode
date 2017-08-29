# Implement int sqrt(int x).
#
# Compute and return the square root of x.


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # old_r = 1
        # diff = 10
        # while diff > 1:
        #     new_r = old_r - (old_r**2 - x)/(2*old_r)
        #     diff = abs(old_r - new_r)
        #     old_r = new_r
        # return old_r


        r = x
        while r*r - x > 0:
            r = (r + x//r)//2
        return int(r)


x = 50
object = Solution()
print(object.mySqrt(x))
