class Solution {
public:
    int trap(vector<int>& height) {
        if(height.size() <= 0) return 0; 
        
        vector<int> left;
        int currentMax = height[0]; 
        for(int i = 0; i < height.size(); i++){
            currentMax = max(currentMax, height[i]);
            left.push_back(currentMax); 
        }
        currentMax = height[height.size()-1];
        vector<int> right; 
        for(int j = height.size() - 1; j >= 0; j--){
            currentMax = std::max(currentMax, height[j]); 
            right.push_back(currentMax); 
        }
        
        std::reverse(right.begin(), right.end());
        
        int water = 0; 
        for(int i = 0; i < height.size(); i++){
            int minHeight = std::min(left[i], right[i]); 
            if(height[i] < minHeight){
                water += (minHeight - height[i]); 
            }
        }
        return water;
    }
};