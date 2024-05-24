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
        index_needle = 0
        index_needle_max = len(needle)
        index_haystack = 0
        while index_haystack < len(haystack):
            if needle[index_needle] == haystack[index_haystack]:
                if index_needle == index_needle_max - 1:
                    return index_haystack - index_needle
                index_needle += 1
                index_haystack += 1

            else:
                index_haystack = index_haystack - index_needle + 1
                index_needle = 0

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
