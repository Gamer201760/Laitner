import sys
from pathlib import Path

import pygame

from core.exception import NotFound


def resource_path(relative: Path) -> Path:
    if hasattr(sys, '_MEIPASS'):
        return Path(sys._MEIPASS, relative)
    return Path(relative)


def load_img(
    path: Path
) -> pygame.Surface:
    path = resource_path(path)
    if not path.exists():
        raise NotFound(path)
    return pygame.image.load(path).convert_alpha()
