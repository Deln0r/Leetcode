func relativeSortArray(arr1 []int, arr2 []int) []int {
    arr2Map := map[int]int{}
    for i, val := range arr2 {
        arr2Map[val] = i
    }

    sort.Slice(arr1, func(i, j int) bool {
        valueA := len(arr2Map)
        valueB := len(arr2Map)
        if val, ok := arr2Map[arr1[i]]; ok {
            valueA = val
        }
        if val, ok := arr2Map[arr1[j]]; ok {
            valueB = val
        }
        if valueA == valueB {
            return arr1[i] < arr1[j]
        }
        return valueA < valueB
    })
    
    return arr1
}