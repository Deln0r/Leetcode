var indp *[]int
var valp *[]int

type ByVal []int

func (b ByVal) Len() int {
	return len(b)
}

func (b ByVal) Swap(i, j int) {
	b[i], b[j] = b[j], b[i]
	(*indp)[i], (*indp)[j] = (*indp)[j], (*indp)[i]
	(*valp)[i], (*valp)[j] = (*valp)[j], (*valp)[i]
}

func (b ByVal) Less(i, j int) bool {
	if (*valp)[i] == (*valp)[j] {
		return (*indp)[i] < (*indp)[j]
	}
	return (*valp)[i] < (*valp)[j]
}

func sortJumbled(mapping []int, nums []int) []int {
	ind := make([]int, len(nums))
	val := make([]int, len(nums))
	indp = &ind
	valp = &val

	for i, v := range nums {
		ind[i] = i
		val[i] = 0

		k := 1
		for {
			val[i] += mapping[(v%(k*10))/k] * k
			k *= 10
			if k > v {
				break
			}
		}
	}

	sort.Sort(ByVal(nums))

	return nums

}