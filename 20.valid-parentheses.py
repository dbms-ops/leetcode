# @lcpr-before-debug-begin

# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30121
#
# [20] 有效的括号
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []
        for i in s:
            if i in hash_map.values():
                stack.append(i)
            else:
                if not stack:
                    return False
                value = stack.pop()
                if hash_map.get(i, "") != value:
                    return False

        return not stack


# @lc code=end


#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

#

# @lcpr case=start
# "([)]"\n
# @lcpr case=end
