import pygame

import core.event
from core.lesson import Lesson


class Card:
    def __init__(
        self,
        screen: pygame.Surface,
        size: list[int],
        border_radius: int,
        text_color: tuple,
        background_color: tuple,
        lesson: Lesson | None = None,
        font_size: int = 14,
        magnet_poses: tuple | None = None,
        magnet_coefficient: int = 30
    ):
        self.screen = screen
        self.size = size
        self.border_radius = border_radius
        self.text_color = text_color
        self.bg_color = background_color
        self.font_size = font_size
        self.magnet_poses = magnet_poses
        self.magnet_k = magnet_coefficient
        self.enable = False
        self.base_size = self.size.copy()

        self.front = ''
        self.back = ''
        self.side = True
        if lesson:
            self.set_lesson(lesson)

    def draw(
        self
    ):
        if self.enable is False:
            return
        if self.lesson is None:
            return
        font = pygame.font.Font(None, self.font_size)
        text = font.render(self.front if self.side else self.back, 1, self.text_color)
        pygame.draw.rect(
            self.screen,
            self.bg_color,
            self.size,
            border_radius=self.border_radius
        )
        self.screen.blit(
            text,
            (
                self.size[2] // 2 - text.get_width() // 2 + self.size[0],
                self.size[3] // 2 - text.get_height() // 2 + self.size[1]
            )
        )

    def move_handler(
        self,
        pos: tuple[int, int],
        rel: tuple[int, int]
    ):
        if self.enable is False:
            return
        if (self.size[0] <= pos[0] <= self.size[0] + self.size[2]) and \
        (self.size[1] <= pos[1] <= self.size[1] + self.size[3]):
            self.size[0] += rel[0]
            self.size[1] += rel[1]

    def update(
        self
    ):
        if self.enable is False:
            return
        if self.magnet_poses is None:
            return

        for i in range(len(self.magnet_poses)):
            if (self.magnet_poses[i][0] - self.magnet_k <= self.size[0] <= self.magnet_poses[i][0] + self.magnet_k) and \
            (self.magnet_poses[i][1] - self.magnet_k <= self.size[1] <= self.magnet_poses[i][1] + self.magnet_k):
                pygame.event.post(self.events[i])
                self.size = self.base_size.copy()

    def set_lesson(
        self,
        lesson: Lesson
    ):
        self.lesson = lesson
        self.events = (
            pygame.event.Event(core.event.NOTREMEMBER_EVENT, lesson=self.lesson),
            pygame.event.Event(core.event.REMEMBER_EVENT, lesson=self.lesson)
        )
        self.enable = True

    def click_handler(
        self,
        pos: tuple[int, int]
    ):
        if self.enable is False:
            return
        if (self.size[0] <= pos[0] <= self.size[0] + self.size[2]) and \
        (self.size[1] <= pos[1] <= self.size[1] + self.size[3]):
            self.side = not self.side

