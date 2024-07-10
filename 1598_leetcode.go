func minOperations(logs []string) int {
	level := 0
	for i := range logs {
		switch logs[i] {
		case "./":
			continue
		case "../":
			if level > 0 {
				level--
			}
		default:
			level++
		}
	}
	return level
}