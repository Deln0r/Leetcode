func fractionAddition(expression string) string {
	var top, bot, numerator, denominator, index int
	bot = 1
	denominator = 1

	for index < len(expression) {
		if index >= len(expression) {
			break
		}
		v := expression[index]
		if v == '/' {
			index++
			temp := string(expression[index])
			index++
			for index < len(expression) && expression[index] != '-' && expression[index] != '+' {
				temp += string(expression[index])
				index++
			}
			i, _ := strconv.Atoi(temp)
			bot = i
			numerator, denominator = cal(top, numerator, bot, denominator)
			continue
		}
		if v != '/' {
			temp := string(v)
			index++
			for index < len(expression) && expression[index] != '/' {
				temp += string(expression[index])
				index++
			}
			i, _ := strconv.Atoi(temp)
			top = i
			continue
		}
	}

	return format(numerator, denominator)
}

func cal(top1, top2, bot1, bot2 int) (int, int) {
	top := (top1 * bot2) + (top2 * bot1)
	bot := bot1 * bot2
	return top, bot
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func format(top, bot int) string {
	temp := top
	if temp < 0 {
		temp *= -1
	}

	divi := gcd(temp, bot)
	top = top / divi
	bot = bot / divi

	return strconv.FormatInt(int64(top), 10) + "/" + strconv.FormatInt(int64(bot), 10)
}