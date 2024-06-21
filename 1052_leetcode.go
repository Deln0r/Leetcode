func maxSatisfied(customers []int, grumpy []int, minutes int) int {
	n := len(customers)
	baseSatisfied := 0

	// Подсчитываем клиентов, которые удовлетворены, когда владелец не раздражительный
	for i := 0; i < n; i++ {
		if grumpy[i] == 0 {
			baseSatisfied += customers[i]
		}
	}

	// Считаем максимальное количество дополнительных удовлетворённых клиентов
	// за любой отрезок длиной 'minutes' используя скользящее окно
	additionalSatisfied := 0
	for i := 0; i < minutes; i++ {
		if grumpy[i] == 1 {
			additionalSatisfied += customers[i]
		}
	}

	maxAdditionalSatisfied := additionalSatisfied

	// Используем скользящее окно для поиска оптимального отрезка времени
	for i := minutes; i < n; i++ {
		if grumpy[i] == 1 {
			additionalSatisfied += customers[i]
		}
		if grumpy[i-minutes] == 1 {
			additionalSatisfied -= customers[i-minutes]
		}
		if additionalSatisfied > maxAdditionalSatisfied {
			maxAdditionalSatisfied = additionalSatisfied
		}
	}

	return baseSatisfied + maxAdditionalSatisfied
}