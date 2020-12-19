class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set <int> setOfIntegers;
        for(int& c : nums){
            if(setOfIntegers.find(c) != setOfIntegers.end())
            {
                return true; 
            }
            else{
                setOfIntegers.insert(c); 
            }
        }
        return false; 
        
    }
};