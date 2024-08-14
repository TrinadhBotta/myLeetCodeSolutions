func topKFrequent(nums []int, k int) []int {
    l := make([][]int, len(nums))

    d := map[int]int{}
    ans := []int{}

    for _, v := range nums {
        if _, found := d[v]; found {
            d[v]++
        } else {
            d[v] = 1
        }
    }

    for key, v := range d {
        l[v-1] = append(l[v-1], key)
    }

    for i := len(l) - 1; i >= 0; i-- {
        for j := len(l[i])-1; j >= 0; j-- {
            k-=1
            ans = append(ans, l[i][j])
            if k==0 {
                return ans
            }
        }
    }

    return []int{}
}