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
    int maxDepth(Node* root) {
        if(root == NULL) return 0; 
        queue<Node*> queue; 
        queue.push(root);
        int depth = 0; 
        while(!queue.empty()){
            int n = queue.size(); 
            for(int i = 0; i < n; i++){
                Node* node = queue.front();
                queue.pop(); 
                if(node->children.size() > 0){
                    for(int i = 0; i < node->children.size(); i++){
                        queue.push(node->children[i]);
                    }
                }
            }
            depth++;
        }
        return depth;
    }
};