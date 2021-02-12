class Solution {
public:
    bool isAnagram(string s, string t) {
        std::sort(s.begin(), s.end());
        std::sort(t.begin(), t.end());
        return s == t; 
    }
};



class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> x;
        for(char& c: s)
        {
            if(x.count(c)){ x[c]++; }
            else{
                x[c] = 1; 
            }
        }
        map<char, int> y; 
        for(char& i: t){
            if(y.count(i)) y[i]++;
            else{
                y[i] = 1; 
            }
        }
        return x == y; 
    }
};