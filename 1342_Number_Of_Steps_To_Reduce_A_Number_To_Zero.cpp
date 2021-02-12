class Solution {
public:
    int numberOfSteps (int num) {
        int s = 0; 
        while(num != 0){
            if(num % 2 == 0) num /= 2;
            else{
                num--; 
            }
            s++;
        }
        return s; 
    }
};


class Solution {
public:
    int numberOfSteps (int num) {
        if(num <= 2) return num; 
        else return num % 2 ? (1+numberOfSteps(num-1)) : (1+numberOfSteps(num / 2)); 
    }
};