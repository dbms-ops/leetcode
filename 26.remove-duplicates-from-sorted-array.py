# @lcpr-before-debug-begin
from python3problem26 import *
from typing import *

# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=26 lang=python3
# @lcpr version=30122
#
# [26] 删除有序数组中的重复项
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:

    def removeDuplicates(self, nums: list[int]) -> (int, list[int]):

        left, right = 0, 1
        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
                right += 1
        return left + 1


# @lc code=end


#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,2,2,3,3,4]\n
# @lcpr case=end
