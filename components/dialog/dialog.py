import pygame

from components.btns.ok import OkBtn
from core.color import TEXT


class Dialog:
    def __init__(
        self,
        screen: pygame.Surface,
    ):
        self.size = (0, 0, 720, 480)
        self.screen = screen
        self.text = ''
        self.btn = OkBtn(
            screen,
            (112, 350, 475, 75)
        )
        self.font_size = 75

    def set_text(
        self,
        text: str
    ):
        self.text = self._split_text(text)

    def handler(
        self,
        pos: tuple[int, int]
    ):
        self.btn.handler(pos)

    def draw(
        self
    ):
        font = pygame.font.Font(None, self.font_size)
        l_f = len(self.text)
        text_pos = self.size[1] + 10
        for i in range(l_f):
            text = font.render(self.text[i], 1, TEXT)
            if i != 0:
                text_pos += self.font_size // 2 + 10

            self.screen.blit(
                text,
                (
                    self.size[2] // 2 - text.get_width() // 2 + self.size[0],
                    text_pos
                )
            )

        self.btn.draw()

    def _split_text(
        self,
        text: str,
        k: int = 20
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
