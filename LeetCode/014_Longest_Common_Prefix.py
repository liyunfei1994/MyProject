"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

输入：strs = ["flower","flow","flight"]
输出："fl"
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        ls = len(strs)
        if ls == 1:
            return strs[0]
        prefix = ''
        pos = 0
        while True:
            try:
                current = strs[0][pos]
            except IndexError:
                break
            index = 1
            while index < ls:
                try:
                    if strs[index][pos] != current:
                        break
                except IndexError:
                    break
                index += 1
            if index == ls:
                prefix = prefix + current
            else:
                break
            pos += 1
        return prefix


    # begin
s = Solution()
print(s.longestCommonPrefix(["flower","flow","fly"]))
