"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
"""

class Solution(object):

    def lengthOfLongestSubstring(self, s):
        charMap = {}
        for i in range(256):
            charMap[i] = -1
        print(charMap)
        ls = len(s)
        i = max_len = 0
        for j in range(ls):
            # Note that when charMap[ord(s[j])] >= i, it means that there are
            # duplicate character in current i,j. So we need to update i.
            print("charMap[ord(s[j])] ", charMap[ord(s[j])])
            if charMap[ord(s[j])] >= i:
                i = charMap[ord(s[j])] + 1
            print("i ", i)
            charMap[ord(s[j])] = j
            max_len = max(max_len, j - i + 1)
            print("max len ", max_len)
            print("=" * 10)
        return max_len

A = Solution()
print(A.lengthOfLongestSubstring("pbbgffd"))
"""
{0: -1, 1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 7: -1, 8: -1, 9: -1, 10: -1, }
charMap[ord(s[j])]  -1
i  0
max len  1
==========
charMap[ord(s[j])]  -1
i  0
max len  2
==========
charMap[ord(s[j])]  1
i  2
max len  2
==========
charMap[ord(s[j])]  -1
i  2
max len  2
==========
charMap[ord(s[j])]  -1
i  2
max len  3
==========
charMap[ord(s[j])]  4
i  5
max len  3
==========
charMap[ord(s[j])]  -1
i  5
max len  3
==========
3
"""