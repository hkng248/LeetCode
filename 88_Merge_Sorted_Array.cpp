//< This solution is atrocious. Its late and I'm tired. 

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        
        if(n == 0) return; 
        
        vector<int> copy = nums1; 
        int l = 0; 
        int r = 0;
        bool lf = false, rf = false; 
        for(int i = 0; i < (m+n); i++)
        {
            int left = -1;
            if(l < m) left = copy[l];
            int right = -1;
            if(r < n) right = nums2[r]; 
            if(l == m){
                lf = true; 
            }
            if(r == n)
            {
                rf = true; 
            }
            
            if(lf && rf == false){
                nums1[i] = right;
                r++; 
                continue; 
            }
            else if(rf && lf == false){
                nums1[i] = left;
                l++; 
                continue; 
            }
            
            if(left < right){
                nums1[i] = left;
                l++; 
            }
            else{
                nums1[i] = right; 
                r++; 
            }
        }
        
    }
};