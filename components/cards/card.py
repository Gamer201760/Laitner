import pygame

from core import event


class Card:
    def __init__(
        self,
        screen: pygame.Surface,
        size: list[int],
        border_radius: int,
        text_color: tuple,
        background_color: tuple,
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
        self.enable = True
        self.base_size = self.size.copy()
        self.events = (
            pygame.event.Event(event.NOTREMEMBER_EVENT),
            pygame.event.Event(event.REMEMBER_EVENT)
        )

        self.front = ''
        self.back = ''
        self.side = True

    def draw(
        self
    ):
        if self.enable is False:
            return
        font = pygame.font.Font(None, self.font_size)
        pygame.draw.rect(
            self.screen,
            self.bg_color,
            self.size,
            border_radius=self.border_radius
        )
        l_f = len(self.front if self.side else self.back)
        text_pos = 0
        for i in range(l_f):
            text = font.render(self.front[i] if self.side else self.back[i], 1, self.text_color)
            if i == 0:
                text_pos = self._first_text(text, l_f)
            else:
                text_pos += self.font_size // 2 + 10
            self.screen.blit(
                text,
                (
                    self.size[2] // 2 - text.get_width() // 2 + self.size[0],
                    text_pos
                )
            )

    def _first_text(
        self,
        text: pygame.Surface,
        n: int
    ):
        return (
            self.size[3] // 2 - text.get_height() // 2 + self.size[1] - ((n - 1) * (self.font_size // 2 + 5) // 2)
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

    def set_text(
        self,
        front: str,
        back: str
    ):
        self.front = self._split_text(front)
        self.back = self._split_text(back)

    def _split_text(
        self,
        text: str,
        k: int = 10
    ) -> list:
        last_pos = 0
        res = []
        for i in range(1, len(text)):
            if last_pos is None:
                break
            near_space = text.find(' ', i * k)
            near_space = None if near_space == -1 else near_space
            res.append(text[last_pos:near_space].strip())
            last_pos = near_space
        return res

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

    def click_handler(
        self,
        pos: tuple[int, int]
    ):
        if self.enable is False:
            return
        if (self.size[0] <= pos[0] <= self.size[0] + self.size[2]) and \
        (self.size[1] <= pos[1] <= self.size[1] + self.size[3]):
            self.side = not self.side

    def set_visible(
        self,
        state: bool
    ):
        self.enable = state

    def is_enable(
        self
    ) -> bool:
        return self.enable

