class Solution {
    public boolean hasDuplicate(int[] nums) {
        int n = nums.length;
        Set<Integer> x = new HashSet<>();
        for(int i=0; i<n; i++)x.add(nums[i]);
        return !(n == x.size());
    }
}