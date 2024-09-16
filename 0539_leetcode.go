import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"math"
)

func findMinDifference(timePoints []string) int {
	// Функция для преобразования времени в минуты
	timeToMinutes := func(t string) int {
		parts := strings.Split(t, ":")
		hours, _ := strconv.Atoi(parts[0])
		minutes, _ := strconv.Atoi(parts[1])
		return hours*60 + minutes
	}

	if len(timePoints) > 1440 { // Если больше 1440 точек, обязательно есть дубликаты (максимум минут в дне - 1440)
		return 0
	}

	// Преобразуем временные точки в минуты
	minutes := make([]int, len(timePoints))
	for i, time := range timePoints {
		minutes[i] = timeToMinutes(time)
	}

	// Сортируем временные точки
	sort.Ints(minutes)

	// Инициализируем минимальную разницу
	minDiff := 1440 // Максимальная разница в минутах в 24-часовом дне

	// Ищем минимальную разницу между соседними точками
	for i := 1; i < len(minutes); i++ {
		diff := minutes[i] - minutes[i-1]
		if diff < minDiff {
			minDiff = diff
		}
	}

	// Учёт разницы между первой и последней точкой (цикл 24 часа)
	firstLastDiff := 1440 - minutes[len(minutes)-1] + minutes[0]
	if firstLastDiff < minDiff {
		minDiff = firstLastDiff
	}

	return minDiff
}