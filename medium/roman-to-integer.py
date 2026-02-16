/*
 * LeetCode Solution: Roman to Integer
 * Difficulty: Medium
 * Language: python
 * URL: https://leetcode.com/problems/roman-to-integer/submissions/1921098567/
 * Date: 16/02/2026, 19:37:58
 * Solution: Initial
 */

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = { "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000 }
        res = 0

        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]

        return res