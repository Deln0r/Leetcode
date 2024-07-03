func intersect(nums1 []int, nums2 []int) (res []int) {
	hm := make(map[int]int)

	// Count the occurrences of each element in nums1
	for _, v := range nums1 {
		hm[v]++
	}

	// Iterate through nums2 and find intersections
	for _, v := range nums2 {
		if count, exists := hm[v]; exists && count > 0 {
			res = append(res, v) // Add the common element to the result
			hm[v]--              // Decrement the count of the element in the hashmap
		}
	}

	return res
}