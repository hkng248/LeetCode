class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        vector<int> colors(graph.size(), 0); 
        queue<int> q; 
        for(int i = 0; i < graph.size(); i++){
            if(colors[i]) continue; 
            colors[i] = 1; 
            q.push(i); 
            while(!q.empty()){
                int temp = q.front(); 
                for(auto neighbor: graph[temp]){
                    if(!colors[neighbor]){
                        colors[neighbor] = -colors[temp]; 
                        q.push(neighbor); 
                    }
                    else if(colors[neighbor] == colors[temp]) return false; 
                }
            q.pop(); 
            }
        }
        return true; 
    }
};