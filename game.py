from pathlib import Path

import pygame

import core.color
import core.event
from btn.lesson import LessonBtn
from btn.load import LoadBtn
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
        self._init_main()

    def _init_main(self):
        self.btns.append(LoadBtn((160, 105, 400, 60), self.screen))
        self.btns.append(LessonBtn((160, 175, 400, 60), self.screen, Path('./example.txt')))
        self.btns.append(LessonBtn((160, 345, 400, 60), self.screen, Path('./english.txt')))

    def _exit(self):
        self.running = False

    def _load_click(self):
        ...

    def _lesson_click(self, path: Path):
        print(path)

    def _mouse_click(self, pos: tuple[int, int], btn: int):
        for i in self.btns:
            i.handler(pos)

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

    def loop(self):
        while self.running:
            self._event()
            self.screen.fill(self.background_color)
            for i in self.btns:
                i.draw()
            pygame.display.flip()

            self.clock.tick(self.fps)
        pygame.quit()
