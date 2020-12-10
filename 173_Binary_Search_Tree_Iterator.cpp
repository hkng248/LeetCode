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
class BSTIterator {
public:
    vector<int> listOfNodes; 
    
    BSTIterator(TreeNode* root) {
        listOfNodes = traverse(root, {}); 
    }
    
    vector<int> traverse(TreeNode* root, vector<int> result)
    {
        if(root == NULL) return result; 
        if(root->left != NULL) result = traverse(root->left, result);
        result.push_back(root->val); 
        if(root->right != NULL) result = traverse(root->right, result); 
        return result; 
    }
    
    int next() {
        int front = listOfNodes.front();
        listOfNodes.erase(listOfNodes.begin());
        return front; 
    }
    
    bool hasNext() {
        return listOfNodes.size() > 0; 
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */