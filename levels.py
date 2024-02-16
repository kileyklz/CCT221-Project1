import pygame

class Level:
    def __init__(self, max_level):
        self.current_level = 1
        self.max_level = max_level
        self.level_texts = {
            1: "Level 1",
            2: "Level 2, Faster",
            3: "Level 3, Faster!!",
            4: "Level 4, Even Faster!!",
            5: "Level 5, Speed!!"
        }

    def increase_level(self):
        if self.current_level < self.max_level:
            self.current_level += 1

    def reset_level(self):
        self.current_level = 1

    def get_ball_speed(self):
        return self.current_level + 1  

    def get_level_text(self):
        return self.level_texts.get(self.current_level, "Level")

level = Level(5) 

level.increase_level()
ball_speed = level.get_ball_speed()
level_text = level.get_level_text()