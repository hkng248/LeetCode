class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        set<int> s(arr.begin(), arr.end()); 
        int index = 1;
        while(true)
        {
            if(s.find(index) == s.end()) k--;
            if(k == 0) return index;
            index++; 
        }
        return -1; 
    }
};
