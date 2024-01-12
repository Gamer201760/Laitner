
import pygame


class Stack:
    def __init__(
        self,
        screen: pygame.Surface,
        size: list[int],
        border_radius: int,
        text_color: tuple,
        background_color: tuple,
        font_size: int = 14,
        shadow: bool = False,
        text: str = '',
        magnet_pos: tuple[int, int] | None = None,
        magnet_k: int = 30
    ):
        self.screen = screen
        self.size = size
        self.border_radius = border_radius
        self.text_color = text_color
        self.bg_color = background_color
        self.font_size = font_size
        self.shadow = shadow
        self.text = text
        self.magnet_pos = magnet_pos
        self.magnet_k = magnet_k

        if shadow:
            self.shadow_size = self.size.copy()
            self.shadow_size[0] -= 5
            self.shadow_size[1] -= 5

            self.shadow_color = pygame.color.Color(self.bg_color)
            hsl = list(self.shadow_color.hsla[:-1])
            hsl[-1] -= 20
            self.shadow_color.hsla = hsl # type: ignore

    def draw(
        self
    ):
        font = pygame.font.Font(None, self.font_size)
        text = font.render(self.text, 1, self.text_color)
        if self.shadow:
            pygame.draw.rect(
                self.screen,
                self.shadow_color,
                self.shadow_size,
                border_radius=self.border_radius
            )
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
