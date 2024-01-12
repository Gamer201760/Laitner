from pygame import Surface

import core.color
from components.cards.stack import Stack


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
            True,
            '-'
        )
