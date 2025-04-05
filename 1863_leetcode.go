func subsetXORSum(nums []int) int {
    n := len(nums)
    subsetCount := 1 << n // 2^n subsets
    totalSum := 0

    // Iterate over all possible subsets
    for subsetMask := 0; subsetMask < subsetCount; subsetMask++ {
        currentXOR := 0
        // Calculate XOR for the current subset
        for i := 0; i < n; i++ {
            if subsetMask&(1<<i) != 0 {
                currentXOR ^= nums[i]
            }
        }
        totalSum += currentXOR
    }

    return totalSum
}