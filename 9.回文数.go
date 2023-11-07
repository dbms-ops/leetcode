/*
 * @lc app=leetcode.cn id=9 lang=golang
 *
 * [9] 回文数
 */

// @lc code=start
package main

func isPalindrome(x int) bool {
	if x == 0 {
		return true
	}
	if x < 0 {
		return false
	}

	if x%10 == 0 {
		return false
	}
	var temp []int
	for x > 0 {
		t := x % 10
		x = x / 10
		temp = append(temp, t)
	}

	if len(temp) == 1 {
		return true
	}

	for i := 0; i < len(temp)/2; i++ {
		if temp[i] != temp[len(temp)-i-1] {
			return false
		}
	}

	return true
}

// @lc code=end
