import (
	"fmt"
	"sort"
)

const MOD = 1000000007

func rangeSum(nums []int, n int, left int, right int) int {
	subarraySums := []int{}

	// Calculate sums of all subarrays
	for i := 0; i < n; i++ {
		currentSum := 0
		for j := i; j < n; j++ {
			currentSum += nums[j]
			subarraySums = append(subarraySums, currentSum)
		}
	}

	// Sort the subarray sums
	sort.Ints(subarraySums)

	// Calculate the sum of elements from index left to right
	result := 0
	for i := left - 1; i < right; i++ {
		result = (result + subarraySums[i]) % MOD
	}

	return result
}