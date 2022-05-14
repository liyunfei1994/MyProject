class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = 0
        table = {}
        start = 0
        for end, v in enumerate(s):
            if v in table.keys():
                start = max(table.get(v) + 1, start)
            print("start", start)
            ans = max(ans, end - start + 1)
            print("ans", ans)
            table[v] = end
            print(table)
        return ans

A = Solution()
print(A.lengthOfLongestSubstring("pwwkew"))