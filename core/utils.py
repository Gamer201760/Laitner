from pathlib import Path

import pygame

from core.exception import NotFound


def load_img(path: Path) -> pygame.Surface:
    if not path.exists():
        raise NotFound(path)
    return pygame.image.load(path).convert_alpha()
