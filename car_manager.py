from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            car.goto(x=300, y=random_y)
            self.cars.append(car)

    def move_cars(self, level):
        for car in self.cars:
            moving_distance = STARTING_MOVE_DISTANCE + (level * MOVE_INCREMENT)
            car.backward(moving_distance)


