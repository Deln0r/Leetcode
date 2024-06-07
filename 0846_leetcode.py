func isNStraightHand(hand []int, groupSize int) bool {
    if len(hand)%groupSize != 0 {
        return false
    }

    count := make(map[int]int)
    for _, card := range hand {
        count[card]++
    }

    sort.Ints(hand)

    for _, startCard := range hand {
        if count[startCard] == 0 {
            continue
        }

        for card := startCard; card < startCard+groupSize; card++ {
            if count[card] == 0 {
                return false
            }
            count[card]--
        }
    }

    return true
}