# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        n -= 1
        convertString = [chr(i) for i in range(ord('A'),ord('Z')+1)]
        base = len(convertString)
        if n < base:
            return convertString[n]
        else:
            return self.convertToTitle(n//base) + convertString[n%base]


object = Solution()
print(object.convertToTitle(300))
