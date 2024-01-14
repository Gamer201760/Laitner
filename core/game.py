from pathlib import Path
from typing import Literal

import pygame

import core.color
import core.event
from components.cards.card import Card
from components.cards.notremember import NotRememberStack
from components.cards.remember import RememberStack
from components.sprites.drag import DragDrop
from core.lesson import Lesson
from core.type import PAGES


class Laitner:
    def __init__(
        self,
        size: tuple[int, int]
    ):
        pygame.init()

        self.size = size
        self.screen = pygame.display.set_mode(size)
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.running = True
        self.background_color = core.color.BACKGROUND

        self.page: PAGES = 'main'
        self.pages = {
            'main': self.main_page,
            'game': self.game_page
        }

        self.dragdrop = pygame.sprite.Group()
        DragDrop(self.dragdrop)

        self.notremember_back = NotRememberStack(
            self.screen,
            [20, 20, 280, 150]
        )

        self.remember_back = RememberStack(
            self.screen,
            [420, 20, 280, 150]
        )

        self.stacks = (
            self.notremember_back,
            self.remember_back
        )

        self.card = Card(
            self.screen,
            [215, 308, 280, 150],
            10,
            (0, 0, 0),
            (217, 217, 217),
            font_size=50,
            magnet_poses=(
                self.notremember_back.size[:2],
                self.remember_back.size[:2]
            )
        )

        self.mark = False
        self.pos = 0

    def _exit(
        self
    ):
        self.running = False
        self.lesson.save()

    def _mouse_click(
        self,
        pos: tuple[int, int],
        btn: int
    ):
        """Click handler"""
        match self.page:
            case 'game':
                self._game_click(pos, btn)

    def _mouse_motion(
        self,
        pos: tuple[int, int],
        rel: tuple[int, int],
        btns: tuple[int, int, int]
    ):
        """Mouse motion handler"""
        match self.page:
            case 'game':
                if btns[0]:
                    self.card.move_handler(pos, rel)

    def _game_click(
        self,
        pos: tuple[int, int],
        btn: int
    ):
        """Click handler for game page"""
        match btn:
            case 1:
                self.card.click_handler(pos)
                self.remember_back.click_handler(pos)
                self.notremember_back.click_handler(pos)

    def _remember_base(
        self,
        mark: Literal['+', '-']
    ):
        self.pos += self.lesson.mark(mark, self.mark, self.pos)
        self._set_text()
        self._shadow_detect(0)
        self._shadow_detect(1)

    def _shadow_detect(
        self,
        i: int
    ):
        if self.lesson.lens[i] > 0:
            self.stacks[i].set_shadow(True)
            return
        self.stacks[i].set_shadow(False)

    def _remember_click_base(
        self,
        mark: bool
    ):
        if self.card.is_enable() is False:
            self.mark = mark
            self.card.set_visible(True)
            self.pos = 0
            self._set_text()

    def _set_text(
        self
    ):
        if self.pos < self.lesson.lens[self.mark]:
            self.card.set_text(*self.lesson.get()[self.mark][self.pos][:2])
            return
        self.card.set_visible(False)

    def _drop(
        self,
        file: str
    ):
        """Drop file handler"""
        self.lesson = Lesson(Path(file))
        self.lesson.load()
        self._set_text()
        self._shadow_detect(0)
        self._shadow_detect(1)
        self.nav('game')

    def _event(
        self
    ):
        """Event handler"""
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self._exit()
                case pygame.MOUSEBUTTONDOWN:
                    self._mouse_click(event.pos, event.button)
                case pygame.DROPFILE:
                    self._drop(event.file)
                case pygame.MOUSEMOTION:
                    self._mouse_motion(event.pos, event.rel, event.buttons)
                case core.event.REMEMBER_EVENT:
                    self._remember_base('+')
                case core.event.NOTREMEMBER_EVENT:
                    self._remember_base('-')
                case core.event.REMEMBER_EVENT_CLICK:
                    self._remember_click_base(True)
                case core.event.NOTREMEMBER_EVENT_CLICK:
                    self._remember_click_base(False)

    def main_page(
        self
    ):
        self.dragdrop.draw(self.screen)

    def game_page(
        self
    ):
        self.card.update()
        self.remember_back.draw()
        self.notremember_back.draw()
        self.card.draw()

    def nav(
        self,
        page: PAGES
    ):
        if self.page != page:
            self.page = page

    def loop(
        self
    ):
        while self.running:
            self._event()
            self.screen.fill(self.background_color)
            self.pages[self.page]()
            pygame.display.flip()

            self.clock.tick(self.fps)
        pygame.quit()
