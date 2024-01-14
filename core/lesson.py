from pathlib import Path
from typing import Literal


class Lesson:
    def __init__(
        self,
        path: Path
    ):
        self.path = path
        self.path_tmp = self.path.with_name(f'.{self.path.name}.tmp')

        self.data: tuple[list[list[str]], list[list[str]]] = ([], [])
        self.marks = ('-', '+')

    def get(
        self
    ) -> tuple[list[list[str]], list[list[str]]]:
        return self.data

    def load(
        self
    ):
        with open(self.path) as f:
            line = f.readline().strip()
            while line != '':
                line = line.split(';')
                if len(line) < 2:
                    continue
                if len(line) == 2:
                    line.append('-')
                self.data[self.marks.index(line[-1])].append(line)
                line = f.readline().strip()
        self.lens = [len(self.data[0]), len(self.data[1])]

    def mark(
        self,
        mark: Literal['+', '-'],
        data: bool,
        pos: int
    ):
        if pos >= self.lens[data]:
            return 0
        if self.data[data][pos][-1] == mark:
            return 1
        self.data[data][pos][-1] = mark
        self.data[not data].append(self.data[data].pop(pos))
        self.lens[data] -= 1
        self.lens[not data] += 1
        return 0

    def save(
        self
    ):
        with open(self.path_tmp, 'w') as f:
            for i in range(max(self.lens)):
                if i < self.lens[0]:
                    f.write(';'.join(self.data[0][i]) + '\n')
                if i < self.lens[1]:
                    f.write(';'.join(self.data[1][i]) + '\n')

        self.path_tmp.rename(self.path.name)
