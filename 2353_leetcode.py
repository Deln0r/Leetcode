class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.heap = defaultdict(list)
        self.foodToCuisine = {}
        self.ratingChange = {}

        for i, cuisine in enumerate(cuisines):
            heappush(self.heap[cuisine], (-ratings[i], foods[i]))
            self.foodToCuisine[foods[i]] = cuisine

    def changeRating(self, food: str, newRating: int) -> None:
        self.ratingChange[food] = -newRating
        cuisine = self.foodToCuisine[food]
        heappush(self.heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while len(self.heap[cuisine]):
            rating, food = self.heap[cuisine][0]
            if food in self.ratingChange and rating != self.ratingChange[food]:
                heappop(self.heap[cuisine])
            else:
                return food
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)