package main

import (
	"fmt"
	"math"
	"strconv"
)

func nearestPalindromic(n string) string {
	num, _ := strconv.Atoi(n)
	length := len(n)

	// Edge cases for numbers like "1", "10", "100", etc.
	if num == 1 {
		return "0"
	}
	if isPowerOf10(num) {
		return strconv.Itoa(num - 1)
	}

	candidates := []int{
		int(math.Pow10(length-1)) - 1, // 99...9 (one less digit)
		int(math.Pow10(length)) + 1,   // 100...01 (one more digit)
	}

	prefix, _ := strconv.Atoi(n[:(length+1)/2])
	for _, delta := range []int{-1, 0, 1} {
		candidate := createPalindrome(prefix+delta, length%2 == 0)
		candidates = append(candidates, candidate)
	}

	closest := -1
	for _, candidate := range candidates {
		if candidate == num {
			continue
		}
		if closest == -1 || abs(candidate-num) < abs(closest-num) || (abs(candidate-num) == abs(closest-num) && candidate < closest) {
			closest = candidate
		}
	}

	return strconv.Itoa(closest)
}

func createPalindrome(prefix int, evenLength bool) int {
	pStr := strconv.Itoa(prefix)
	var palindrome string
	if evenLength {
		palindrome = pStr + reverseString(pStr)
	} else {
		palindrome = pStr + reverseString(pStr[:len(pStr)-1])
	}
	result, _ := strconv.Atoi(palindrome)
	return result
}

func reverseString(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func isPowerOf10(x int) bool {
	for x > 1 {
		if x%10 != 0 {
			return false
		}
		x /= 10
	}
	return true
}

func main() {
	fmt.Println(nearestPalindromic("123")) // Output: "121"
	fmt.Println(nearestPalindromic("1"))   // Output: "0"
	fmt.Println(nearestPalindromic("10"))  // Output: "9"
	fmt.Println(nearestPalindromic("100")) // Output: "99"
}
