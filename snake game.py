import tkinter as tk
import random

# Constants
WIDTH = 400
HEIGHT = 400
DELAY = 150
SIZE = 20
START_X = WIDTH // 2 // SIZE * SIZE
START_Y = HEIGHT // 2 // SIZE * SIZE

class SnakeGame(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("Snake Game")
        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.snake = [(START_X, START_Y)]
        self.direction = "Right"
        self.food = self.create_food()
        self.score = 0
        self.delay = DELAY
        self.game_over = False
        self.bind("<Key>", self.on_key_press)
        self.update()

    def update(self):
        if not self.game_over:
            self.move_snake()
            self.check_collision()
            self.draw_snake()
            self.draw_food()
            self.update_score()
            self.after(self.delay, self.update)

    def draw_snake(self):
        self.canvas.delete("snake")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill="green", tag="snake")

    def draw_food(self):
        self.canvas.delete("food")
        x, y = self.food
        self.canvas.create_oval(x, y, x + SIZE, y + SIZE, fill="red", tag="food")

    def move_snake(self):
        x, y = self.snake[0]
        if self.direction == "Up":
            y -= SIZE
        elif self.direction == "Down":
            y += SIZE
        elif self.direction == "Left":
            x -= SIZE
        elif self.direction == "Right":
            x += SIZE
        self.snake.insert(0, (x, y))
        self.snake.pop()

    def check_collision(self):
        x, y = self.snake[0]
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            self.end_game()
        elif self.snake[0] in self.snake[1:]:
            self.end_game()
        elif self.snake[0] == self.food:
            self.score += 1
            self.snake.append((0, 0))  # Add a new segment to the snake
            self.food = self.create_food()
            if self.score % 5 == 0:
                self.increase_speed()

    def create_food(self):
        x = random.randint(0, WIDTH // SIZE - 1) * SIZE
        y = random.randint(0, HEIGHT // SIZE - 1) * SIZE
        return x, y

    def increase_speed(self):
        self.delay -= 10

    def update_score(self):
        self.title(f"Snake Game - Score: {self.score}")

    def end_game(self):
        self.game_over = True
        self.canvas.create_text(
            WIDTH // 2, HEIGHT // 2,
            text="Game Over",
            font=("Arial", 20),
            fill="red"
        )

    def on_key_press(self, event):
        if event.keysym == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif event.keysym == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif event.keysym == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif event.keysym == "Right" and self.direction != "Left":
            self.direction = "Right"


if _name_ == "_main_":
    game = SnakeGame()
    game.mainloop()
