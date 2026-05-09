


class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen;

        for(int num: nums){

            auto result = seen.insert(num);
            cout<< *result.first << " " << result.second << " " << endl;

            if(!result.second){
                return true;
            }
        }
        return false;
    }
};