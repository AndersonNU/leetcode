# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# For example,
# Given nums = [0, 1, 3] return 2.

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if nums == [0]:
        #     return 1
        # List = list(range(len(nums)+1))
        # for i in range(len(List)):
        #     if i in nums:
        #         del List[i]
        #     else:
        #         return i
        x = list(range(len(nums)+1))
        y = nums
        x.extend(y)
        res = 0
        for num in x:
            res ^= num
        return res


nums = [0,1,2,4]
# nums = [0]
object = Solution()
print(object.missingNumber(nums))
