/*
 * LeetCode Solution: M[i,j] --> M'[j,N-1-i]
 * Difficulty: Medium
 * Language: python
 * URL: https://leetcode.com/problems/rotate-image/submissions/1920122433/
 * Date: 15/02/2026, 19:42:56
 * Solution: Initial
 */

void rotate(vector<vector<int>>& matrix) {
       int n=matrix.size();

       for (int i =0; i<n-1; i++){
        for(int j=i+1; j<n; j++){
            swap (matrix[i][j], matrix[j][i]);
        }
       } 
       for (int i =0; i<n; i++){
        reverse(matrix[i].begin(), matrix[i].end());
       }
    }
};
public:
class Solution {