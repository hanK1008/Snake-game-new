from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()                       # Creating Screen
screen.setup(width=600, height=600)     # Setting screen window size
screen.bgcolor("black")                 # setting fill color of screen
screen.title("My snake game")           # Screen title name will change to given string
screen.tracer(0)                        # Animation will get off
snake = Snake()                         # Creating snake from our snake file
food = Food()                           # Creating food from our food file
score = Score()                         # Creating scoreboard from our score file


game_on = True                          # Defining switch for our game to make game our for certain conditions

# start listening to keyboard input on for arrow keys
screen.listen()                         # Command for starting turtle screen to take inputs if given
screen.onkey(snake.up, "Up")            # command for UP arrow key
screen.onkey(snake.down, "Down")        # Command for Down arrow key
screen.onkey(snake.right, "Right")      # Command for Right arrow key
screen.onkey(snake.left, "Left")        # Command for left arrow key

while game_on:                          # Starting loop to make continue moving of snake
    screen.update()                     # Will update screen after every snake move one bit
    sleep(0.1)                         # Set speed of snake lower the number higher the speed
    snake.move()                        # Move the snake one bit
    # Detect collision with food
    if snake.head.distance(food) < 17:  # Take distance between snake head and food.....and if conditions met
        food.refresh()                  # Create new food on screen
        score.score_update()            # Will update the score by 1 point
        snake.extend()                  # Will add 1 snake block to the end of the snake

    # Detect collision with wall
    # Will measure the position of head of the snake from all corners of the screen
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False                 # Will make game over by flipping switch
        score.game_over()               # Will show the message GAME OVER on the screen

    # Detect collision with itself (tail)
    for snake_piece in snake.snake_blocks[1:]:
        # Started from second piece of snake
        # as first position is same as snake.head
        if snake.head.distance(snake_piece) < 10:
            game_on = False
            score.game_over()


screen.exitonclick()
