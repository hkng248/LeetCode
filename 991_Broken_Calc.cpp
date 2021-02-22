class Solution {
public:
    int brokenCalc(int X, int Y) {
        if(X == Y) return 0;
        else if( X > Y) return X - Y; 
        else if (Y % 2 == 0) Y /= 2; 
        else{
            Y++;
        }
        return 1 + brokenCalc(X, Y); 
    }
};