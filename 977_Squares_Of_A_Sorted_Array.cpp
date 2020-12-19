class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> result; 
        for(int& c: nums){
            result.push_back(c*c); 
        }
        sort(result.begin(), result.end()); 
        return result; 
        
    }
};