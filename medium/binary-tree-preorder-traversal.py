/*
 * LeetCode Solution: Binary Tree Preorder Traversal
 * Difficulty: Medium
 * Language: python
 * URL: https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/1978397403/
 * Date: 14/04/2026, 21:03:50
 * Solution: Initial
 */

result.push_back(node->val);

            if (node->right) st.push(node->right);
            if (node->left) st.push(node->left);
        }

        return result;
    }
};