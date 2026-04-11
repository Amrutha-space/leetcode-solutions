/*
 * LeetCode Solution: Minimum Distance Between Three Equal Elements II
 * Difficulty: Medium
 * Language: python
 * URL: https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/submissions/1975606179/?envType=daily-question&envId=2026-04-11
 * Date: 11/04/2026, 22:22:01
 * Solution: Initial
 */

if (v.size() >= 3) {
                int n = v.size();
                mind = min(mind, 2 * (v[n-1] - v[n-3]));
            }
        }

        return mind == INT_MAX ? -1 : mind;
    }
};