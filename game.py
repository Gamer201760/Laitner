from pathlib import Path

import pygame

import core.color
import core.event
from btn.lesson import LessonBtn
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

        self.btns: list[Button] = []
        self.btns_coords = [160, 35, 400, 60]

    def _exit(self):
        self.running = False

    def _load_click(self):
        print('load')

    def _lesson_click(self, path: Path):
        print(path)

    def _mouse_click(self, pos: tuple[int, int], btn: int):
        for button in self.btns:
            button.handler(pos)

    def _drop(self, file: str):
        self.btns_coords[1] += 70
        self.btns.append(LessonBtn(tuple(self.btns_coords), self.screen, Path(file))) # type: ignore

    def _event(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self._exit()
                case pygame.MOUSEBUTTONDOWN:
                    self._mouse_click(event.pos, event.button)
                case core.event.LOAD_CLICK:
                    self._load_click()
                case core.event.LESSON_CLICK:
                    self._lesson_click(event.path)
                case pygame.DROPFILE:
                    self._drop(event.file)

    def loop(self):
        while self.running:
            self._event()
            self.screen.fill(self.background_color)
            for button in self.btns:
                button.draw()
            pygame.display.flip()

            self.clock.tick(self.fps)
        pygame.quit()
