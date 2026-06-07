class Solution {
    public int[] twoSum(int[] nums, int target) {
        int arrs[] = {0,0};
        for(int i = 0; i<nums.length-1; i++){
            for(int j = i+1; j<nums.length; j++){
                if(nums[i] + nums[j] == target){
                    arrs[0] = i;
                    arrs[1] = j;
                    return arrs;
                }
            }
        }
        return arrs;
    }
}
