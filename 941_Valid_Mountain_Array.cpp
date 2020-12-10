class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        if(arr.size() < 3) return false;
        bool increasing = true; 
        if(arr[0] > arr[1]) return false;
        for(int i = 1; i < arr.size(); i++){
            if((arr[i] > arr[i-1]) && increasing){
                continue; 
            }
            else if(arr[i] == arr[i-1]){
                return false;
            }
            else if(arr[i] < arr[i-1] && increasing){
                increasing = false; 
            }
            else if(arr[i] < arr[i-1] && increasing == false){
                continue;
            }
            else if(arr[i] > arr[i-1]  && increasing == false)
            {
                return false; 
            }
        }
        if(increasing) return false;
        return true; 
    }
};