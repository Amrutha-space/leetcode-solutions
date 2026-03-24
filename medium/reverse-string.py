/*
 * LeetCode Solution: Reverse String
 * Difficulty: Medium
 * Language: python
 * URL: https://leetcode.com/problems/reverse-string/submissions/1958048870/
 * Date: 24/03/2026, 23:02:31
 * Solution: Initial
 */

class Solution {
public:
    void reverseString(vector<char>& s) {
        int st=0, end = s.size()-1;

        while (st<end){
            swap(s[st++], s[end--]);
        }
    }
};