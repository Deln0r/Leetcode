type Cash struct {
	Five   int
	Ten    int
	Twenty int
}

func lemonadeChange(bills []int) bool {
	cash := Cash{}
	for _, bill := range bills {
		switch bill {
		case 5:
			cash.Five++
		case 10:
			if cash.Five == 0 {
				return false
			} else {
				cash.Five--
				cash.Ten++
			}
		case 20:
			if cash.Five == 0 || cash.Ten == 0 {
				if cash.Five > 2 {
					cash.Five = cash.Five - 3
					continue
				}
				return false
			} else {
				cash.Five--
				cash.Ten--
				cash.Twenty++
			}
		}

	}

	return true
}