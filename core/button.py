import pygame


class Button():
    def __init__(
            self,
            size: tuple[int, int, int, int],
            screen: pygame.Surface,
            text_color: tuple[int, int, int],
            background_color: tuple[int, int, int],
            event: pygame.event.Event,
            font_size: int = 14,
            text: str = ''
    ) -> None:
        self.size = size
        self.screen = screen
        self.text_color = text_color
        self.background_color = background_color
        self.event = event
        self.font_size = font_size
        self.text = text

    def draw(self):
        font = pygame.font.Font(None, self.font_size)
        text = font.render(self.text, 1, self.text_color)
        pygame.draw.rect(self.screen, self.background_color, self.size, border_radius=10)
        self.screen.blit(
            text,
            (
                self.size[2] // 2 - text.get_width() // 2 + self.size[0],
                self.size[3] // 2 - text.get_height() // 2 + self.size[1]
            )
        )

    def handler(self, pos: tuple[int, int]):
        if (self.size[0] <= pos[0] <= self.size[0] + self.size[2]) and \
            (self.size[1] <= pos[1] <= self.size[1] + self.size[3]):
            pygame.event.post(self.event)
