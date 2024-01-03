from pathlib import Path

import pygame

from core.utils import load_img


class DragDrop(pygame.sprite.Sprite):
    def __init__(self, *groups) -> None:
        super().__init__(*groups)
        self.image = load_img(Path('./resources/drag-drop.svg'))
        self.rect = self.image.get_rect()
        self.rect.x = 120
