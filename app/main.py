class Car:
    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        power_to_mark_raw = self.clean_power - car.clean_mark
        power_to_mark = (power_to_mark_raw
                         if power_to_mark_raw != 0
                         else 1)
        rating_to_distance = (self.average_rating
                              / self.distance_from_city_center)
        return round(car.comfort_class * power_to_mark * rating_to_distance, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_power > car.clean_mark:
            car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        sum_of_ratings = self.average_rating * self.count_of_ratings + rating
        self.average_rating = round(sum_of_ratings
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
