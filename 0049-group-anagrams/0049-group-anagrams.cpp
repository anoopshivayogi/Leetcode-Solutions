#include<unordered_map>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // Solution 1 
        // Time - O(nlogn)
        // Space - O()

        unordered_map<string, vector<string>> groups;
        for(auto& word : strs){
            string key = word;
            sort(key.begin(), key.end());
            groups[key].push_back(word);
        }

        vector<vector<string>> result;
        for(auto& pair : groups){
            result.push_back(pair.second);
        }
        
        return result;
        
    }
};