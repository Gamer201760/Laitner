import pygame


class Laitner:
    def __init__(self, size: tuple[int, int]) -> None:
        pygame.init()

        self.size = size
        self.screen = pygame.display.set_mode(size)
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.running = True

