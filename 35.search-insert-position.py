#
# @lc app=leetcode.cn id=35 lang=python3
# @lcpr version=30122
#
# [35] 搜索插入位置
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # 二分查找
        left, right = 0, len(nums) - 1
        if target <= nums[left]:
            return left
        if target > nums[right]:
            return right + 1
        while right - left != 1:
            middle = (left + right) // 2
            if target > nums[middle]:
                left = middle
            elif target < nums[middle]:
                right = middle
            else:
                return middle
        return left + 1


# @lc code=end


#
# @lcpr case=start
# [1,3,5,6]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n7\n
# @lcpr case=end

#
