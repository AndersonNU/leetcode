# Given a collection of distinct numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]



class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # perms = [[]]
        # for n in nums:
        #     new_perms = []
        #     for perm in perms:
        #         for i in range(len(perm) + 1):
        #             new_perms.append(perm[:i] + [n] + perm[i:])  ###insert n
        #             # print('new_perms is:', new_perms)
        #     perms = new_perms
        # return perms
        from itertools import permutations
        l = list(permutations(nums))

        return l
nums = [1,2,3,4,5,6,8,0]
x = Solution()
print(x.permute(nums))