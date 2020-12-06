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
    bool hasPathSum(TreeNode* root, int sum) {
        vector<int> paths; 
        paths = hasPath(root, 0, paths);
        if(paths.size() > 0){
            return std::find(paths.begin(), paths.end(), sum) != paths.end(); 
        }
        return false; 
    }
    
    vector<int> hasPath(TreeNode* root, int length, vector<int> paths)
    {
        if(root == NULL) return paths;
        length += root->val; 
        if(root->left != NULL) paths = hasPath(root->left, length, paths);
        if(root->right != NULL) paths = hasPath(root->right, length, paths); 
        if(root->left == NULL && root->right == NULL){
            paths.push_back(length); 
        }
        return paths; 
    }
};