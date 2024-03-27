# @lcpr-before-debug-begin
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=14 lang=python3
# @lcpr version=30120
#
# [14] 最长公共前缀
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if "" in strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        start = strs[0]

        for i in range(1, len(start) + 1):
            sub_str = start[:i]
            for item in strs:
                if not item.startswith(sub_str):
                    return sub_str[: i - 1]
        return start

# @lc code=end


#
# @lcpr case=start
# ["flower","flow","flight"]\n
# @lcpr case=end

# @lcpr case=start
# ["dog","racecar","car"]\n
# @lcpr case=end


# @lcpr case=start
# ["","","a"]\n
# @lcpr case=end

# @lcpr case=start
# ["flower","flower","flower","flower"]\n
# @lcpr case=end
