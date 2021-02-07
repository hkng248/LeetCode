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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result; 
        if(root == NULL) return result; 
    
        queue<TreeNode*> x; 
        x.push(root); 
        while(!x.empty()){
            vector<int> level; 
            int size = x.size(); 
            for(int i = 0; i < size; i++){
                TreeNode* c = x.front();
                level.push_back(c->val);
                x.pop();
                if(c->left != NULL) x.push(c->left); 
                if(c->right != NULL) x.push(c->right); 
            }
            result.push_back(level[level.size() - 1]); 
        }
        return result; 
    }
};