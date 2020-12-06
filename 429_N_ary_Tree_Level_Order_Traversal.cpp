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

//< Iterative solution using a queue 
class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>> result;
        if(root == NULL) return result;
        
        queue<Node*> queue; 
        queue.push(root); 
        while(!queue.empty()){
            vector<int> level;
            int n = queue.size(); //< you have to get the size of the queue before you start adding children
            for(int i = 0; i < n; i++){
                Node* node = queue.front();
                level.push_back(node->val);
                queue.pop();
                if(node->children.size() > 0 ){
                    for(int i = 0; i < node->children.size(); i++){
                        queue.push(node->children[i]); 
                    }
                }
            }
            result.push_back(level); 
        }
        return result; 
    }
};



//< Recursive solution 
class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        map<int, vector<int>> levels; 
        levels = breadthFirstSearch(root, levels, 0); 
        vector<vector<int>> result; 
        for(auto const& c: levels){
            result.push_back(c.second); 
        }
        return result; 
    }
    
    map<int, vector<int>> breadthFirstSearch(Node* root, map<int, vector<int>> levels, int level){
        if(root == NULL) return levels;
        levels[level].push_back(root->val); 
        if(root->children.size() > 0){
            for(int i = 0; i < root->children.size(); i++){
                levels = breadthFirstSearch(root->children[i], levels, level+1); 
            }
        }
        return levels; 
    }
};