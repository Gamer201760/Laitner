import pygame
import core.color
from core.button import Button


class Laitner:
    def __init__(self, size: tuple[int, int]) -> None:
        pygame.init()

        self.size = size
        self.screen = pygame.display.set_mode(size)
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.running = True
        self.background_color = core.color.BACKGROUND

        self.btn = Button((100, 100, 200, 100), self.screen, (255, 255, 255), (255, 0, 0), font_size=100, text='Test')

    def _exit(self):
        self.running = False

    def _mouse_click(self, pos: tuple[int, int], btn: int):
        self.btn.handler(pos)
        print(pos, btn)

    def _event(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self._exit()
                case pygame.MOUSEBUTTONDOWN:
                    self._mouse_click(event.pos, event.button)

    def loop(self):
        while self.running:
            self._event()
            self.screen.fill(self.background_color)
            self.btn.draw()
            pygame.display.flip()

            self.clock.tick(self.fps)
        pygame.quit()
