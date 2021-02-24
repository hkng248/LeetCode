class Solution {
public:
    bool canFormArray(vector<int>& arr, vector<vector<int>>& pieces) {
        map<int,  vector<int>> keys;
        for(int i = 0; i < pieces.size(); i++)
        {
            keys[pieces[i][0]] = pieces[i]; 
        }
        
        while(arr.size() > 0)
        {
            int front = arr[0]; 
            if(keys.find(front) != keys.end())
            {
                for(int& j : keys[front]){
                    if(j == arr[0])
                    {
                        arr.erase(arr.begin()); //< C++ does not have a pop_front method 
                    }
                    else{
                        return false; 
                    }
                }

            }
            else{
                return false; 
            }
        }
        return arr.size() == 0; 
    }
    
};