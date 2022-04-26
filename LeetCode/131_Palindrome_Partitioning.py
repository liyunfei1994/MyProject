"""
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

回文串 是正着读和反着读都一样的字符串。
切割问题也可以抽象为一棵树形结构图
递归用来纵向遍历，for循环用来横向遍历，切割线切割到字符串的末尾位置。
"""
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # https://discuss.leetcode.com/topic/6186/java-backtracking-solution/2
        result = [] # 收集全部的结果
        curr = [] # 收集单一的结果
        start = 0

        # 结果就在叶子结点 参数需要start，因为不能重复切割
        self.recurPartition(result, curr, s, start) # 0表示start index，从剩下的子串切割
        return result

    def recurPartition(self, result, curr, s, start):
        # 没有字符，返回空列表
        # print("=" * 5)
        # print("for 循环外 start = ", start)
        if start == len(s):
            result.append(list(curr))
        # 开始递归+回溯
        for i in range(start, len(s)):
            # print("i = ", i)
            # print("start = ", start)
            if self.isPalindrome(s, start, i):
                # print("是回文数")
                curr.append(s[start:i + 1])
                # print("curr ", curr)
                # print("进入递归")
                self.recurPartition(result, curr, s, i + 1)
                # print("跳出递归，执行下一步")
                # pop的作用是在树里面能往回走，再走另一个树枝
                curr.pop()
            #     print("执行pop")
            #     print("curr pop ", curr)
            # print("执行完一次for循环") # for循环执行了7次，7个节点，每个节点执行一次for循环


    def isPalindrome(self, s, begin, end):
        while begin < end:
            if s[begin] != s[end]:
                return False
            begin += 1
            end -= 1
        return True

A = Solution()
print(A.partition("aab"))