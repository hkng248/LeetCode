/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<int> postorder(Node* root) {
        vector<int> values;
        return postorderTraversal(root, values); 
    }
    
    vector<int> postorderTraversal(Node* root, vector<int> values){
        if(root == NULL) return values; 
        if(root->children.size() > 0){
            for(int i = 0; i < root->children.size(); i++){
                values = postorderTraversal(root->children[i], values);
            }
        }
        values.push_back(root->val);
        return values; 
    }
};