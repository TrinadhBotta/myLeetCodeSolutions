func twoSum(nums []int, target int) []int {
    d := map[int]int{}
    
    for i := range nums{
        idx, found := d[target-nums[i]]
        if found{
            return []int{idx,i}
        }
        d[nums[i]] = i
    }
    return []int{}
}