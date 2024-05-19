#
# @lc app=leetcode.cn id=13 lang=python3
# @lcpr version=30202
#
# [13] 罗马数字转整数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 3,
            "IX": 8,
            "XL": 30,
            "XC": 80,
            "CD": 300,
            "CM": 800,
        }
        return sum(
            hash_map.get(s[max(index-1, 0):index + 1], hash_map.get(value))
            for index, value in enumerate(s)
        )


# @lc code=end


#
# @lcpr case=start
# "III"\n
# @lcpr case=end

# @lcpr case=start
# "IV"\n
# @lcpr case=end

# @lcpr case=start
# "IX"\n
# @lcpr case=end

# @lcpr case=start
# "LVIII"\n
# @lcpr case=end

# @lcpr case=start
# "MCMXCIV"\n
# @lcpr case=end

#
