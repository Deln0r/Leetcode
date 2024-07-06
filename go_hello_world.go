package main

import "fmt"

func isMonotonic(array []int) bool {
	if len(array) <= 2 {
		return true // Слайс из 0, 1 или 2 элементов всегда монотонный
	}

	isNonDecreasing := true
	isNonIncreasing := true

	for i := 1; i < len(array); i++ {
		if array[i] < array[i-1] {
			isNonDecreasing = false
		}
		if array[i] > array[i-1] {
			isNonIncreasing = false
		}
	}

	return isNonDecreasing || isNonIncreasing // Монотонный, если хотя бы одно условие выполняется
}

func main() {
	testCases := [][]int{
		{1, 7},
		{1, 1},
		{3, 3, 1},
		{9, 5, 1},
		{23, 5, 23},
	}

	for _, arr := range testCases {
		fmt.Printf("%v - %t\n", arr, isMonotonic(arr))
	}
}
