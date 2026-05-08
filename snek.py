"""
Snek
My high score is 78. Can you beat it?!
"""

import tkinter as tk
import random

# CONFIG
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
CELL_SIZE = 20

GRID_WIDTH = WINDOW_WIDTH // CELL_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // CELL_SIZE

GAME_SPEED = 100  # milliseconds

BG_COLOR = "black"
SNEK_HEAD_COLOR = "lime"
SNEK_BODY_COLOR = "green"
FOOD_COLOR = "red"
TEXT_COLOR = "white"

# GAME CLASS

class SnekGame:

    def __init__(self, root):
        self.root = root
        self.root.title("Snake? Snake! SNAAAAAAAAAAAAKE!!!")

        self.canvas = tk.Canvas(
            root,
            width=WINDOW_WIDTH,
            height=WINDOW_HEIGHT,
            bg=BG_COLOR,
            highlightthickness=0
        )
        self.canvas.pack()

        self.score_label = tk.Label(
            root,
            text="Score: 0",
            font=("Arial", 14),
            fg=TEXT_COLOR,
            bg="gray20"
        )
        self.score_label.pack(fill=tk.X)

        # Key bindings
        self.root.bind("<Up>", lambda e: self.change_direction("UP"))
        self.root.bind("<Down>", lambda e: self.change_direction("DOWN"))
        self.root.bind("<Left>", lambda e: self.change_direction("LEFT"))
        self.root.bind("<Right>", lambda e: self.change_direction("RIGHT"))
        self.root.bind("r", lambda e: self.restart_game())

        self.running = True
        self.after_id = None
        self.restart_game()

    # GAME SETUP

    def restart_game(self):

        # Stop previous game loop if one exists
        if self.after_id is not None:
            self.root.after_cancel(self.after_id)
            self.after_id = None

        self.canvas.delete("all")

        self.score = 0
        self.direction = "RIGHT"
        self.running = True

        # Snek starts in center
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2

        self.snek = [
            (start_x, start_y),
            (start_x - 1, start_y),
            (start_x - 2, start_y)
        ]

        self.spawn_food()
        self.update_score()

        self.draw()

        self.game_loop()

    # FOOD

    def spawn_food(self):
        while True:
            food = (
                random.randint(0, GRID_WIDTH - 1),
                random.randint(0, GRID_HEIGHT - 1)
            )

            if food not in self.snek:
                self.food = food
                break

    # INPUT

    def change_direction(self, new_direction):

        opposites = {
            "UP": "DOWN",
            "DOWN": "UP",
            "LEFT": "RIGHT",
            "RIGHT": "LEFT"
        }

        if opposites[new_direction] != self.direction:
            self.direction = new_direction

    # GAME UPDATE

    def move_snek(self):

        head_x, head_y = self.snek[0]

        if self.direction == "UP":
            head_y -= 1
        elif self.direction == "DOWN":
            head_y += 1
        elif self.direction == "LEFT":
            head_x -= 1
        elif self.direction == "RIGHT":
            head_x += 1

        new_head = (head_x, head_y)

        # Wall collision
        if (
            head_x < 0 or
            head_x >= GRID_WIDTH or
            head_y < 0 or
            head_y >= GRID_HEIGHT
        ):
            self.game_over()
            return

        # Self collision
        if new_head in self.snek:
            self.game_over()
            return

        # Move snek
        self.snek.insert(0, new_head)

        # Food collision
        if new_head == self.food:
            self.score += 1
            self.update_score()
            self.spawn_food()
        else:
            self.snek.pop()

    # DRAWING

    def draw(self):

        self.canvas.delete("all")

        # Draw food
        fx, fy = self.food

        self.canvas.create_rectangle(
            fx * CELL_SIZE,
            fy * CELL_SIZE,
            (fx + 1) * CELL_SIZE,
            (fy + 1) * CELL_SIZE,
            fill=FOOD_COLOR,
            outline=""
        )

        # Draw snek
        for index, (x, y) in enumerate(self.snek):

            color = (
                SNEK_HEAD_COLOR
                if index == 0
                else SNEK_BODY_COLOR
            )

            self.canvas.create_rectangle(
                x * CELL_SIZE,
                y * CELL_SIZE,
                (x + 1) * CELL_SIZE,
                (y + 1) * CELL_SIZE,
                fill=color,
                outline=""
            )

    # SCORE

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

    # GAME OVER

    def game_over(self):

        self.running = False

        self.canvas.create_text(
            WINDOW_WIDTH // 2,
            WINDOW_HEIGHT // 2 - 20,
            text="GAME OVER",
            fill=TEXT_COLOR,
            font=("Arial", 28, "bold")
        )

        self.canvas.create_text(
            WINDOW_WIDTH // 2,
            WINDOW_HEIGHT // 2 + 20,
            text="Press 'R' to Restart",
            fill=TEXT_COLOR,
            font=("Arial", 16)
        )

    # MAIN LOOP

    def game_loop(self):

        if self.running:

            self.move_snek()

            # Only continue if game still running
            if self.running:

                self.draw()

                self.after_id = self.root.after(
                    GAME_SPEED,
                    self.game_loop
                )

# MAIN

if __name__ == "__main__":

    root = tk.Tk()
    root.configure(bg="gray20")

    game = SnekGame(root)

    root.mainloop()