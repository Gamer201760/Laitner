from pathlib import Path
from typing import Literal

from file import File


class Lesson(File):
    def __init__(self, path: Path) -> None:
        super().__init__(path)

    def get_background(self) -> Path | None:
        line = self.file.readline()
        if 'setting_background' in line:
            return Path(line[line.find('=') + 1:])
        self.file.seek(0)

    def get(self) -> list[str]:
        raw = self.readline()
        if len(raw) == 0:
            self.seek(0)
            raw = self.readline()
        return raw.split(';')

    def mark(self, mark: Literal['+', '-']):
        line = self.line.split(';')

        if len(line) == 3:
            line[-1] = mark
        else:
            line.append(mark)

        self.write(';'.join(line) + '\n')

if __name__ == '__main__':
    load = Lesson(Path('./example.txt'))
    for i in range(1, 8):
        print(load.get())
        load.mark('+')
    load.close()
