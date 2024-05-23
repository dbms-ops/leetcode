# @lcpr-before-debug-begin


# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=28 lang=python3
# @lcpr version=30122
#
# [28] 找出字符串中第一个匹配项的下标
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for index, value in enumerate(haystack):
            if haystack[index:index + len(needle)] == needle:
                return index
        return -1

# @lc code=end


#
# @lcpr case=start
# "sadbutsad"\n"sad"\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n"leeto"\n
# @lcpr case=end

#
