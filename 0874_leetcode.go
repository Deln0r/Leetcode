func robotSim(commands []int, obstacles [][]int) int {
	directions := []direction{
		{
			x: 0,
			y: 1,
		},
		{
			x: 1,
			y: 0,
		},
		{
			x: 0,
			y: -1,
		},
		{
			x: -1,
			y: 0,
		},
	}

	obs := make(map[direction]int, len(obstacles))
	for i := 0; i < len(obstacles); i++ {
		dir := direction{
			x: obstacles[i][0],
			y: obstacles[i][1],
		}
		obs[dir] = 0
	}

	pos := direction{
		x: 0,
		y: 0,
	}

	curIndex := 0
	maxDis := 0

	for i := 0; i < len(commands); i++ {
		val := commands[i]
		curDirection := directions[curIndex]
		if val >= 0 {
			if curDirection.x != 0 {
				for j := 0; j < val; j++ {
					dir := direction{
						x: pos.x + curDirection.x,
						y: pos.y,
					}
					if _, ok := obs[dir]; !ok {
						pos.x += curDirection.x

						if pos.x*pos.x+pos.y*pos.y > maxDis {
							maxDis = pos.x*pos.x + pos.y*pos.y
						}
					} else {
						break
					}
				}
			} else {
				for j := 0; j < val; j++ {
					dir := direction{
						x: pos.x,
						y: pos.y + curDirection.y,
					}
					if _, ok := obs[dir]; !ok {
						pos.y += curDirection.y

						if pos.x*pos.x+pos.y*pos.y > maxDis {
							maxDis = pos.x*pos.x + pos.y*pos.y
						}
					} else {
						break
					}
				}
			}
		} else {
			if val == -1 {
				curIndex += 1
				if curIndex == 4 {
					curIndex = 0
				}
			} else {
				curIndex -= 1
				if curIndex == -1 {
					curIndex = 3
				}
			}
		}
	}

	return maxDis
}

type (
	// (0, 1) north (1, 0) east (-1, 0) west (0, -1) south
	direction struct {
		x int
		y int
	}
)