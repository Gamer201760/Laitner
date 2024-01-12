import fileinput
from pathlib import Path
from typing import Iterator


class Lesson:
    def __init__(
        self,
        path: Path
    ):
        self.file = fileinput.input(
            path,
            inplace=True,
        )

        self.remember: list[tuple[str, str]] = []
        self.not_remember: list[tuple[str, str]] = []

        self.data: tuple[Iterator, Iterator] = (
            iter(self.remember),
            iter(self.not_remember)
        )

    def get(
        self
    ) -> tuple[Iterator, Iterator]:
        return self.data
