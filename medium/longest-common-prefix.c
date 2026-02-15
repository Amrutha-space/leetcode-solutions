/*
 * LeetCode Solution: Longest Common Prefix
 * Difficulty: Medium
 * Language: c
 * URL: https://leetcode.com/problems/longest-common-prefix/submissions/1920211581/
 * Date: 15/02/2026, 21:39:30
 * Solution: Initial
 */

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]

        return res