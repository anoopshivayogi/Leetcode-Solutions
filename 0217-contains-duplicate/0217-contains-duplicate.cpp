#include <unordered_set>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {

        // solution 1 - using unordered_set
        // time - O(n)
        // space - O(1)

        // unordered_set<int> seen;
        // for(int num: nums){

        //     auto result = seen.insert(num);
        //     cout<< *result.first << " " << result.second << " " << endl;

        //     if(!result.second){
        //         return true;
        //     }
        // }
        // return false;



        // solution 2 - using sort
        // time - O(nlogn)
        // space - O(1)

        sort(nums.begin(), nums.end());

        for(int i=1; i< nums.size(); i++){
            if(nums[i] == nums[i-1]){
                return true;
            }
        }
        return false;
    }

};