/*
 * LeetCode Solution: Regular Expression Matching
 * Difficulty: Medium
 * Language: python
 * URL: https://leetcode.com/problems/regular-expression-matching/submissions/1949088357/
 * Date: 15/03/2026, 18:24:26
 * Solution: Initial
 */

for(int j = 2; j <= n; j++) {
        int n = p.length();

        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));

        dp[0][0] = true;
            if(p[j-1] == '*') {
                dp[0][j] = dp[0][j-2];
            }
        int m = s.length();
    bool isMatch(string s, string p) {