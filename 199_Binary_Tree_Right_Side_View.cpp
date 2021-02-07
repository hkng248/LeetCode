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
        if(root == NULL) return result ;
        queue<TreeNode*> q; 
        q.push(root);
        while(!q.empty()){
            int size = q.size(); 
            int last = NULL; 
            for(int i = 0; i < size; i++){
                TreeNode* c = q.front();
                q.pop(); 
                if(c->left != NULL) q.push(c->left);
                if(c->right != NULL) q.push(c->right); 
                last = c->val; 
            }
            result.push_back(last); 
        }
        return result; 
    }
};