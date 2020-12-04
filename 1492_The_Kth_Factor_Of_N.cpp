class Solution {
public:
    int kthFactor(int n, int k) {
        vector<int> factors = {1}; 
        int i = 2;
        while( i <= n){
            if( n % i == 0){
                factors.push_back(i); 
            }
            i++;
        }
        if(k <= factors.size())
        {
            return factors[k-1]; 
        }
        return -1; 
    }
};