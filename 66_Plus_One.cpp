class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        return plusOneHelper(digits, digits.size() - 1); 
    }
    
    vector<int> plusOneHelper(vector<int> digits, int index){
        if(index < 0){
            auto it = digits.insert(digits.begin(), 1); 
            return digits; 
        }
        if(digits[index] + 1 == 10){
            digits[index] = 0;
            return plusOneHelper(digits, index - 1); 
        }
        else{
            digits[index]++; 
        }
        return digits; 
    }
};