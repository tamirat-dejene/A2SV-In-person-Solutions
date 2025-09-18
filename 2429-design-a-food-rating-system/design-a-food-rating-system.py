class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.store = defaultdict(list) # food: Heap(-rating, food)
        self.ratings = defaultdict(int) # food: rating
        self.cuisines = defaultdict(str) # food: cuisine

        for i in range(len(foods)):
            food, cuisine, rating = foods[i], cuisines[i], ratings[i]

            heappush(self.store[cuisine], (-rating, food))
            self.ratings[food] = rating
            self.cuisines[food] = cuisine

    def changeRating(self, food: str, newRating: int) -> None:
        if self.ratings[food] == newRating:
            return

        self.ratings[food] = newRating
        heappush(self.store[self.cuisines[food]], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while self.store[cuisine] and -self.store[cuisine][0][0] != self.ratings[self.store[cuisine][0][1]]:
            heappop(self.store[cuisine])
        
        return self.store[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)