#include <algorithm>

class Solution {
public:
    bool isAnagram(string s, string t) {
        // solution 1 - using sort technique
        

        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        return s == t;

        
    }
};