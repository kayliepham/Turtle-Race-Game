import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.onkey(key="Up", fun=turtle.move_up)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars(scoreboard.level - 1)

    # detect if turtle has completed level
    if turtle.is_at_finish_line():
        scoreboard.level_up()
        turtle.reset_player()

    # detect collision with car
    for car in car_manager.cars:
        if turtle.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()