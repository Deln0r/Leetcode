func singleNumber(nums []int) []int {
	// Шаг 1: Находим XOR всех чисел в массиве
	xor := 0
	for _, num := range nums {
		xor ^= num
	}

	// Шаг 2: Находим любой бит, который равен 1 в полученном XOR
	// Этот бит должен быть установлен в одном из одиноковых чисел, но не в обоих
	bit := xor & -xor

	// Шаг 3: Разделяем числа на два группы: одну, в которой этот бит установлен,
	// и другую, в которой он не установлен
	result := []int{0, 0}
	for _, num := range nums {
		if num&bit == 0 {
			result[0] ^= num
		} else {
			result[1] ^= num
		}
	}

	// Шаг 4: XOR чисел в каждой группе, чтобы получить одиноковые числа
	return result
}