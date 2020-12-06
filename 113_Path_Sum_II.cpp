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
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> paths;
        return hasPaths(root, {}, 0, sum, paths);
    }

    vector<vector<int>> hasPaths(TreeNode* root, vector<int> level, int start, int target,  vector<vector<int>> paths){
        if(root == NULL) return paths; 
        start += root->val; 
        level.push_back(root->val); 
        if(root->left != NULL)
        {
            paths = hasPaths(root->left, level,start, target, paths); 
        }
        if(root->right != NULL)
        {
            paths = hasPaths(root->right, level,start, target, paths);
        }
        if(root->left == NULL && root->right == NULL){
            if(target == start) paths.push_back(level); 
        }
        return paths; 
    }
};