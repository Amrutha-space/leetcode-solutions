/*
 * LeetCode Solution: Reverse Integer
 * Difficulty: Medium
 * Language: python
 * URL: https://leetcode.com/problems/reverse-integer/submissions/1925940058/
 * Date: 21/02/2026, 10:16:31
 * Solution: Initial
 */

class Solution {
public:
    int reverse(int n) {
        int revNum = 0; 
        while (n != 0) {
            int lastdig = n % 10;
            if (revNum > INT_MAX / 10 || revNum < INT_MIN / 10)
                return 0;
                
            revNum = revNum * 10 + lastdig;
            n = n / 10;