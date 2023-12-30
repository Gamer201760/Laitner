from pathlib import Path


class Lesson:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.file = open(self.path)
        self.bg = self.get_background()

    def _get_raw(self) -> list[str]:
        return self.file.readlines(40)

    def get_background(self) -> Path | None:
        line = self.file.readline()
        if 'setting_background' in line:
            return Path(line[line.find('=') + 1:])

    def get(self) -> list[list[str]]:
        return list(map(lambda x: x.strip().split(';'), self._get_raw()))

    def close(self) -> None:
        self.file.close()


if __name__ == '__main__':
    load = Lesson(Path('./example.txt'))
    print(load.bg)
    print(load.get())
    load.close()
