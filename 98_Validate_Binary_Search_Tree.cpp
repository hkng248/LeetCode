/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return validateTree(root, -1, -1); 
    }
    bool validateTree(TreeNode* root, int left, int right)
    {
        if(root == NULL) return true;
        if((left != -1 && left >= root->val) || (right != -1 && right <= root->val))
        {
            return false; 
        }
        return validateTree(root->left, left, root->val) && validateTree(root->right, root->val, right); 
    }
};