import pygame
import core.color
from core.button import Button


class LoadBtn(Button):
    def __init__(
        self,
        size: tuple[int, int, int, int],
        screen: pygame.Surface,
    ) -> None:
        super().__init__(size, screen, core.color.TEXT, core.color.BTN_BACKGROUND, 100, 'Загрузить')
