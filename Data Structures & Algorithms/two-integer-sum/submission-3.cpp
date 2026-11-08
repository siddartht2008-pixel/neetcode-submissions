class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int,int> d;
        for(int i=0;i<nums.size();i++){
            d[target -nums[i]]=nums[i];
        }
        int a = 0;
        for(int i=0;i<nums.size();i++){
            if (d.count(nums[i])){
                a = i;

            }
        }
        int b = 0;
        for(int i=0;i<nums.size();i++){
            if (nums[i]==target-nums[a] and i!= a){
               b = i;
            }
        }
        if (a<b){
            return{a,b};
        }
        else{
            return {b,a};
        }
    }
};     
        