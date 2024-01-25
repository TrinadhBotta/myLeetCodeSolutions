class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> d = new HashMap<>();
        for (int i = 0; i<nums.length; i++){
            int sd = target - nums[i];
            if (d.containsKey(sd)) {
                return new int[]{d.get(sd), i};
            }
            d.put(nums[i],i);
        }
        return new int[]{-1, -1};
    }
}