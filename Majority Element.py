<<<<<<< HEAD
# Given an array of size n, find the majority element. The majority element is the element that
# appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.

=======
# Given an array of size n, find the majority element. The majority element is the element that appears
# more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.


>>>>>>> refs/remotes/leetcode/master
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
<<<<<<< HEAD
=======
        if len(nums) <= 1:
            return nums[0]
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] in my_dict:
                my_dict[nums[i]] += 1
                # print(my_dict)
                if my_dict[nums[i]] > len(nums)/2:
                    # print(my_dict[nums[i]], len(nums)/2)
                    return nums[i]
            else:
                my_dict[nums[i]] = 1

        # THis is better solution
        count = 0
        for i in range(len(nums)):
            if count == 0:
                count += 1
                major = nums[i]
            elif major == nums[i]:
                count += 1
            else:
                count -= 1
        return major
>>>>>>> refs/remotes/leetcode/master
