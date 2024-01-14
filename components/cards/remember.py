import pygame
from pygame import Surface

import core.color
from components.cards.stack import Stack
from core.event import REMEMBER_EVENT_CLICK


class RememberStack(Stack):
    def __init__(
        self,
        screen: Surface,
        size: list[int],
    ):
        super().__init__(
            screen,
            size,
            10,
            core.color.TEXT,
            core.color.REMEMBER_BG,
            150,
            True,
            '+',
            event=pygame.event.Event(REMEMBER_EVENT_CLICK)
        )
