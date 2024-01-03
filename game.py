
import pygame

import core.color
import core.event
from components.sprites.drag import DragDrop


class Laitner:
    def __init__(self, size: tuple[int, int]) -> None:
        pygame.init()

        self.size = size
        self.screen = pygame.display.set_mode(size)
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.running = True
        self.background_color = core.color.BACKGROUND

        self.dragdrop = pygame.sprite.Group()
        DragDrop(self.dragdrop)

    def _exit(self):
        self.running = False

    def _load_click(self):
        print('load')

    def _mouse_click(self, pos: tuple[int, int], btn: int):
        ...

    def _drop(self, file: str):
        print(file)

    def _event(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self._exit()
                case pygame.MOUSEBUTTONDOWN:
                    self._mouse_click(event.pos, event.button)
                case core.event.LOAD_CLICK:
                    self._load_click()
                case pygame.DROPFILE:
                    self._drop(event.file)

    def loop(self):
        while self.running:
            self._event()
            self.screen.fill(self.background_color)
            self.dragdrop.draw(self.screen)

            pygame.display.flip()

            self.clock.tick(self.fps)
        pygame.quit()
