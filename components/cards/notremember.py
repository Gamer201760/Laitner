import pygame
from pygame import Surface

import core.color
from components.cards.stack import Stack
from core.event import NOTREMEMBER_EVENT_CLICK


class NotRememberStack(Stack):
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
            core.color.NOTREMEMBER_BG,
            150,
            False,
            '-',
            event=pygame.event.Event(NOTREMEMBER_EVENT_CLICK)
        )
