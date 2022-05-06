class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        temp = s.split(' ')
        print(temp)
        temp = [t for t in temp if len(t) > 0]
        print(temp)
        if len(temp) == 0:
            return 0
        else:
            return len(temp[-1])


A = Solution()
print(A.lengthOfLastWord(s="hello me  "))
