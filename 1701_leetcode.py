func averageWaitingTime(customers [][]int) float64 {
    clock := 0
    total := 0
    for _, order := range customers {
        clock = max(clock, order[0])+order[1]
        total += (clock - order[0])
    }

    return float64(total)/float64(len(customers))
}