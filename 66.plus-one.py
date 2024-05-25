#
# @lc app=leetcode.cn id=66 lang=python3
# @lcpr version=30202
#
# [66] 加一
#
# https://leetcode.cn/problems/plus-one/description/
#
# algorithms
# Easy (45.78%)
# Likes:    1391
# Dislikes: 0
# Total Accepted:    745.1K
# Total Submissions: 1.6M
# Testcase Example:  '[1,2,3]'
#
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
#
#
# 示例 1：
#
# 输入：digits = [1,2,3]
# 输出：[1,2,4]
# 解释：输入数组表示数字 123。
#
#
# 示例 2：
#
# 输入：digits = [4,3,2,1]
# 输出：[4,3,2,2]
# 解释：输入数组表示数字 4321。
#
#
# 示例 3：
#
# 输入：digits = [0]
# 输出：[1]
#
#
#
#
# 提示：
#
#
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        while index >= 0:
            if digits[index] != 9:
                digits[index] += 1
                break
            else:
                digits[index] = 0
                index -= 1

        if index == -1:
            digits.insert(0, 1)

        return digits

# @lc code=end

#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#
