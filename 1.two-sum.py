#
# @lc app=leetcode.cn id=1 lang=python3
# @lcpr version=30202
#
# [1] 两数之和
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for index, x in enumerate(nums):
            if target - x in hash_map:
                return [hash_map.get(target - x), index]
            hash_map[x] = index


# @lc code=end

#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end
