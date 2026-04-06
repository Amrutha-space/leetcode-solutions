/*
 * LeetCode Solution: Comprehensive Next Permutation Intuition(w/Algo) Explanation
 * Difficulty: Medium
 * Language: python
 * URL: https://leetcode.com/problems/next-permutation/submissions/1970802347/
 * Date: 06/04/2026, 22:46:44
 * Solution: Initial
 */

class Solution {
public:
    void nextPermutation(vector<int>& a) {
        int ind = -1;
        int n = a.size();
 
        for (int i = n - 2; i >= 0; i--) {
            if (a[i] < a[i + 1]) {
                ind = i;
                break;
            }