#include <algorithm>

class Solution {
public:
    bool isAnagram(string s, string t) {
        // Solution 1 - using sort technique

        // sort(s.begin(), s.end());
        // sort(t.begin(), t.end());


        // for(int i=0; i<s.size(); i++){
        //     cout << s[i] - 'a';
        // }

        // return s == t;


        // Solution 2 - using frequency count

        if(s.size() != t.size()){
            return false;
        }
        
        int count[26] = {0};

        for(int i=0; i<s.size(); i++){
            count[s[i] - 'a']++;
        }

        for(int i=0; i<t.size();i++){
            count[t[i] - 'a']--;
        }

        for(int i=0; i<26; i++){
            if(count[i] != 0){
                return false;
            }
        }

        return true;
    }
};