# @lcpr-before-debug-begin
from python3problem9 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=9 lang=python3
# @lcpr version=30202
#
# [9] 回文数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        if x == 0:
            return True
        # 从左向右读一遍,从右向左读一遍,对比下是否相等

        num_list = []

        while x > 0:
            num_list.append(x % 10)
            x //= 10

        for i in range(len(num_list)):
            j = len(num_list) - i - 1
            if num_list[i] != num_list[j]:
                return False
            if i >= j:
                return True
        return False


# @lc code=end


#
# @lcpr case=start
# 121\n
# @lcpr case=end

# @lcpr case=start
# -121\n
# @lcpr case=end

# @lcpr case=start
# 10\n
# @lcpr case=end

#
