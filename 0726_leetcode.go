type Formula interface {
	counts() map[string]int
	String() string
}

type SimpleFormula struct {
	element string
	count   int
}

func (f SimpleFormula) String() string {
	return fmt.Sprintf("%s: %d", f.element, f.count)
}

func (f SimpleFormula) counts() map[string]int {
	return map[string]int{f.element: f.count}
}

type ComplexFormula struct {
	elements []Formula
	count    int
}

func (f ComplexFormula) String() string {
	counts := f.counts()
	var keys []string
	for k, _ := range counts {
		keys = append(keys, k)
	}

	sort.Strings(keys)
	s := ""
	for _, k := range keys {
		if counts[k] == 1 {
			s += k
		} else {
			s += fmt.Sprintf("%s%d", k, counts[k])
		}
	}

	return s
}

func (f ComplexFormula) counts() map[string]int {
	s := make(map[string]int)

	for _, e := range f.elements {
		eCounts := e.counts()
		for k, v := range eCounts {
			s[k] = s[k] + (v * f.count)
		}
	}

	return s
}

func countOfAtoms(formula string) string {
	i := 0
	parsedFormula := ComplexFormula{count: 1}

	for i < len(formula) {
		f, read := readFormula(formula[i:])
		i += read
		parsedFormula.elements = append(parsedFormula.elements, f)
	}

	return fmt.Sprint(parsedFormula)
}

func readFormula(formula string) (Formula, int) {
	e, readE, isComplex := readElement(formula)
	c, readC := readCount(formula[readE:])

	if isComplex {
		i := 1
		var formulas []Formula
		for i < len(e)-1 {
			f, readF := readFormula(e[i : len(e)-1])
			i += readF
			formulas = append(formulas, f)
		}
		return ComplexFormula{
			elements: formulas,
			count:    c,
		}, readE + readC
	} else {
		return SimpleFormula{
			element: e,
			count:   c,
		}, readE + readC
	}
}

func readElement(formula string) (string, int, bool) {
	element := ""
	if formula[0] == '(' {
		element = "("
		open := 1
		i := 1
		for open > 0 {
			element += string(formula[i])
			if formula[i] == '(' {
				open += 1
			} else if formula[i] == ')' {
				open -= 1
			}

			i += 1
		}
		return element, len(element), true
	}

	if !isUpper(formula[0]) {
		panic("NOT UPPERCASE: " + string(formula[0]))
	}

	element = string(formula[0])
	i := 1
	for i < len(formula) && isLower(formula[i]) {
		element += string(formula[i])
		i += 1
	}

	return element, len(element), false
}

func readCount(formula string) (int, int) {
	if len(formula) == 0 || !isNum(formula[0]) {
		return 1, 0
	}

	num := ""
	i := 0
	for i < len(formula) && isNum(formula[i]) {
		num += string(formula[i])
		i += 1
	}

	n, _ := strconv.Atoi(num)
	return n, len(num)
}

func isUpper(c byte) bool {
	return c >= 'A' && c <= 'Z'
}

func isNum(c byte) bool {
	return c >= '0' && c <= '9'
}

func isLower(c byte) bool {
	return c >= 'a' && c <= 'z'
}