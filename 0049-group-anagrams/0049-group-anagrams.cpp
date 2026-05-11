#include<unordered_map>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // Solution 1 
        // Time - O(nlogn)
        // Space - O(logn) - the space used for recursive calls in c++ implementation of sort()

        // unordered_map<string, vector<string>> groups;
        // for(auto& word : strs){
        //     string key = word;
        //     sort(key.begin(), key.end());
        //     groups[key].push_back(word);
        // }

        // vector<vector<string>> result;
        // for(auto& pair : groups){
        //     result.push_back(pair.second);
        // }
        
        // return result;


        // Solution 2
        // Time - 
        // Space - 

        unordered_map<string, vector<string>> groups;

        for(auto& word : strs){
            int count[26] = {0};

            for(char c : word){
                count[c - 'a']++;
            }

            // build from the count

            string key = "";
            for(int i=0; i<26; i++){
                key += to_string(count[i]) + "#";
            }

            groups[key].push_back(word);

        }


        vector<vector<string>> result;

        for(auto& pair : groups){
            result.push_back(pair.second);
        }


        return result;
        
    }
};