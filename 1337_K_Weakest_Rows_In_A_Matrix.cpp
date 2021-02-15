class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        map<int, vector<int>> x; 
        int index = 0; 
        for(int i = 0; i < mat.size(); i++){
            int z = count(mat[i].begin(), mat[i].end(), 1); 
            x[z].push_back(i);  
        }
        
        // C++ (elements in std::map are ordered by default by the operator >> applied to the key)
        vector<int> result; 
        map<int, vector<int>>::iterator it;
        for(it = x.begin(); it != x.end(); it++){
            while((k > 0) && (!it->second.empty())){
                int l = it->second.front();
                result.push_back(l);
                it->second.erase(it->second.begin()); 
                k--;
            }
        }
        return result; 
    }
};