from pathlib import Path

import pygame

import core.color
from core.button import Button
from core.event import LESSON_CLICK


class LessonBtn(Button):
    def __init__(
        self,
        size: tuple[int, int, int, int],
        screen: pygame.Surface,
        path: Path
    ) -> None:
        super().__init__(
            size,
            screen,
            core.color.TEXT,
            core.color.BTN_BACKGROUND,
            pygame.event.Event(LESSON_CLICK, path=path),
            50,
            path.name
        )
