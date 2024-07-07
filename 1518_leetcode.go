func numWaterBottles(numBottles int, numExchange int) int {
	res := numBottles

	for numBottles/numExchange > 0 {
		res += numBottles / numExchange
		numBottles = numBottles/numExchange + numBottles%numExchange
	}

	return res
}