import "strings"

var myMap = map[int]string{
	1:          "One ",
	2:          "Two ",
	3:          "Three ",
	4:          "Four ",
	5:          "Five ",
	6:          "Six ",
	7:          "Seven ",
	8:          "Eight ",
	9:          "Nine ",
	10:         "Ten ",
	11:         "Eleven ",
	12:         "Twelve ",
	13:         "Thirteen ",
	14:         "Fourteen ",
	15:         "Fifteen ",
	16:         "Sixteen ",
	17:         "Seventeen ",
	18:         "Eighteen ",
	19:         "Nineteen ",
	20:         "Twenty ",
	30:         "Thirty ",
	40:         "Forty ",
	50:         "Fifty ",
	60:         "Sixty ",
	70:         "Seventy ",
	80:         "Eighty ",
	90:         "Ninety ",
	100:        "Hundred ",
	1000:       "Thousand ",
	1000000:    "Million ",
	1000000000: "Billion ",
}

func numberToWords(num int) string {
	if num == 0 {
		return "Zero"
	}
	result := ""
	if num >= 1000000000 {
		result = myMap[num/1000000000] + myMap[1000000000]
		num = num % 1000000000
	}
	if num >= 1000000 {
		triple := num / 1000000
		result += triples(triple) + myMap[1000000]
		num = num % 1000000
	}
	if num >= 1000 {
		triple := num / 1000
		result += triples(triple) + myMap[1000]
		num = num % 1000
	}
	if num > 0 {
		result += triples(num)
	}

	return strings.Trim(result, " ")
}

func triples(num int) string {
	result := ""

	if num >= 100 {
		result += myMap[num/100] + myMap[100]
		num = num % 100
	}
	if num > 20 {
		result += myMap[(num/10)*10] + myMap[(num%10)]
	} else {
		result += myMap[num]
	}

	return result
}