/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        if(original == NULL || cloned == NULL) return NULL; 
        vector<TreeNode*> queue; 
        queue.push_back(cloned); 
        while(queue.size() > 0){
            TreeNode* current = queue[0];
            queue.erase(queue.begin());
            if(current->val == target->val){ return current; }
            if(current->left != NULL){ queue.push_back(current->left);}
            if(current->right != NULL){ queue.push_back(current->right); }
        }
        return NULL; 
    }
};