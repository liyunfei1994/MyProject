"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

 输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
"""

class Solution(object):
    # 动态规划
    """
    这道题需要反向思考，即从后往前考虑。假设dp[i]表示爬上第i层台阶所有的方案数，
    根据题目要求，我们一次只能爬1层台阶或者2层台阶。

    如果我们选择最后一步只爬一层台阶，到达第i层，则这种情况一共有dp[i-1]种方案，
    因为我们一定是从第i − 1 i-1i−1层爬1层台阶上来的，因此有dp[i-1]种方法。
    如果我们选择最后一步爬两层台阶，到达第i层，同理，这种情况共有dp[i-2]种方案，
    因为只能在dp[i-2]的每种方案末尾加上2阶才能实现爬两层台阶到达第i ii层。
    所以，由上面的分析我们就可以写出本题的状态转移方程：dp[i] = dp[i-1] + dp[i-2]
    我们注意到，其实对于每个n > 2 ,它的方案数量都只跟n − 1 与n − 2 有关系，
    所以我们可以使用滑动窗口的方法使得额外开销从一个大小为n + 1的数组优化为O(1)
        int climbStairs(int n){
        if(n <= 2){
            return n;
        }
        int p = 1, q = 2, r = 0;//初始化滑动窗口
        for(int i = 3; i < n; i++){
            r = p + q;
            p = q;
            q = r;//上面动画演示的过程，即窗口滑动的过程
        }
        return r;
    }
    """

    def climbStairs(self, n):
        if n <= 1:
            return 1
        dp = [1] * 2
        print("dp", dp)
        for i in range(2, n + 1):
            dp[1], dp[0] = dp[1] + dp[0], dp[1]
            print("dp", dp)
        return dp[1]

A = Solution()
print(A.climbStairs(n=3))