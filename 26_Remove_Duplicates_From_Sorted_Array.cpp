class Solution {
public:
    int removeDuplicates(vector<int>& nums) {   
        if(nums.size() == 0) return 0; 
        int index = 1, lastNum = nums[0]; 
        for(int i = 1; i < nums.size(); i++)
        {
            if(nums[i] == lastNum){
                
            }
            else{
                nums[index] = nums[i]; 
                lastNum = nums[i]; 
                index++; 
            }
        }
        return index; 
    }
};