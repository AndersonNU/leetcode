# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
        for key, val in dict.items():
            if val == 1:
                return key
        # ==========this doesn't work because of time limits'============
        # List = []
        # for num in nums:
        #     if num in List:
        #         del List[List.index(num)]
        #     else:
        #         List.append(num)
        # return List[0]

List = [1,0,0,1,2,3,2,4,4]
# List = [-1]
object = Solution()
print(object.singleNumber(List))
