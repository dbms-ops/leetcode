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
        while True:
            if s[:-1] == " ":
                s = s[:-1]
            else:
                break

        start = len(s)
        count = 0
        while start != 0:
            start -= 1
            if s[start] != " ":
                count += 1
            else:
                break
        return count


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
