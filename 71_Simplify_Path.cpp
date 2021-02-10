class Solution {
public:
    string simplifyPath(string path) {
        string r, s; 
        stack<string> stack; 
        stringstream ss(path); 
        
        while(getline(ss, s, '/')){
            if(s == "" || s == ".") continue; 
            if(s == ".." && !stack.empty()) stack.pop(); 
            else if (s != "..") stack.push(s); 
        }
        
        while(!stack.empty()){
            r = "/" + stack.top() + r; 
            stack.pop(); 
        }
        return r.empty() ? "/" : r; 
        
    }
};