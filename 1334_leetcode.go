func findTheCity(n int, edges [][]int, distanceThreshold int) int {
	var dis [][]int = make([][]int, n)
	for i := 0; i < n; i++ {
		dis[i] = make([]int, n)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			dis[i][j] = 1000000
		}
		dis[i][i] = 0
	}
	for _, e := range edges {
		dis[e[0]][e[1]] = e[2]
		dis[e[1]][e[0]] = e[2]
	}
	// fmt.Println(dis)
	for k := 0; k < n; k++ {
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				if dis[i][k]+dis[k][j] < dis[i][j] {
					dis[i][j] = dis[i][k] + dis[k][j]
				}
			}
		}
	}

	var maxCnt, cityInd int = 1000, -1
	for i := 0; i < n; i++ {
		var tmpCnt int = 0
		for j := 0; j < n; j++ {
			if dis[i][j] <= distanceThreshold {
				tmpCnt++
			}
		}
		if tmpCnt <= maxCnt {
			maxCnt = tmpCnt
			cityInd = i
		}
	}
	return cityInd
}