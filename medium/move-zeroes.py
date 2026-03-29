/*
 * LeetCode Solution: Move Zeroes
 * Difficulty: Medium
 * Language: python
 * URL: https://leetcode.com/problems/move-zeroes/submissions/1963085218/
 * Date: 29/03/2026, 22:53:32
 * Solution: Initial
 */

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
        int j = -1;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                j = i;
                break;
            }
        }