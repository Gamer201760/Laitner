import pygame
from pygame import Surface

from components.btns.button import Button
from core.color import BTN_BACKGROUND, TEXT
from core.event import DIALOG_OK_EVENT


class OkBtn(Button):
    def __init__(
        self,
        screen: Surface,
        size: tuple[int, int, int, int]
    ):
        super().__init__(
            screen,
            size,
            TEXT,
            BTN_BACKGROUND,
            pygame.event.Event(DIALOG_OK_EVENT),
            90,
            'Ok'
        )
