func maxDistance(position []int, m int) int {
	sort.Ints(position)
	return sort.Search(position[len(position)-1]/(m-1), func(distance int) bool {
		cnt, pre := 1, position[0] // always select the first bucket
		for i := 1; i < len(position) && cnt < m; i++ {
			if position[i]-pre > distance { // select the buckets greedily
				cnt++
				pre = position[i]
			}
		}
		return cnt < m
	})
}