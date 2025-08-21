#
# @lc app=leetcode id=2138 lang=python3
#
# [2138] Divide a String Into Groups of Size k
#

# @lc code=start
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        output = []
        for i in range(0, len(s), k):
            part = s[i:i+k]
            while len(part) < k:
                part += fill
            output.append(part)
        return output
# @lc code=end

