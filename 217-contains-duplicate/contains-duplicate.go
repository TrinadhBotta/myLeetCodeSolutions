func containsDuplicate(nums []int) bool {
    n := map[int]int{}

    for k, v := range nums{
        _, found := n[v]
        if found{
            return true
        }
        n[v] = k
    }
    return  false
}