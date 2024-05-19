#
# @lc app=leetcode.cn id=21 lang=python3
# @lcpr version=30121
#
# [21] 合并两个有序链表
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        preprev = ListNode(val=-1)
        prev = preprev
        while list1.next and list2.next:
            if list1.val > list2.val:
                prev.next = list2
                list2 = list2.next
            else:
                prev.next = list1
                list1 = list1.next

        return preprev.next


# @lc code=end


#
# @lcpr case=start
# [1,2,4]\n[1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[0]\n
# @lcpr case=end

#
