from enum import Enum

class Sides(Enum):
    TOP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Launcher:
    def __init__(self, name, icon, command):
        self.name = name
        self.icon = icon
        self.command = command
        self.is_running = False
