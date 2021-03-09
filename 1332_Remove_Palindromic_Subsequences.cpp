class Solution {
public:
    int removePalindromeSub(string s) {
        if(s.length() == 0) return 0; 
        string c = s;
        reverse(c.begin(), c.end());
        if ( c == s) return 1; 
        return 2; 
        
    }
};