#
# @lc app=leetcode.cn id=58 lang=python3
# @lcpr version=30122
#
# [58] 最后一个单词的长度
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 倒序
        index = len(s)-1
        while s[index] == ' ':
            index -= 1
        word_count = 0

        while index >= 0 and s[index] != " ":
            index -= 1
            word_count += 1

        return word_count


# @lc code=end


#
# @lcpr case=start
# "Hello World"\n
# @lcpr case=end

# @lcpr case=start
# "   fly me   to   the moon  "\n
# @lcpr case=end

# @lcpr case=start
# "luffy is still joyboy"\n
# @lcpr case=end
