#include<unordered_map>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // Solution 1 

        unordered_map<string, vector<string>> groups;
        for(auto& word : strs){
            string key = word;
            sort(word.begin(), word.end());
            groups[word].push_back(key);
        }

        vector<vector<string>> result;
        for(auto& pair : groups){
            result.push_back(pair.second);
        }
        
        return result;
        
    }
};