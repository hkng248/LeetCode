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
    TreeNode* increasingBST(TreeNode* root) {
        vector<int> c; 
        vector<int> values = inorder(root, c);
        
        std::sort(values.begin(), values.end());
        TreeNode* newRoot = new TreeNode(values[0]); 
        TreeNode* head = newRoot; 
        for(int i = 1; i < values.size(); i++) 
        {
            newRoot->right = new TreeNode(values[i]); 
            newRoot = newRoot->right; 
        }
        return head; 

    }
    
    vector<int> inorder(TreeNode* root, vector<int> values){
        if(root == NULL) return values;
        values = inorder(root->left, values); 
        values.push_back(root->val);
        values = inorder(root->right, values);
        return values; 
    }
};