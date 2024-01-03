from pathlib import Path


class File:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.tmp_path = self.path.with_name(f'.{self.path.name}.tmp')

        self.file = open(self.path)
        self.tmp = open(self.tmp_path, 'w')

        self.line = ''

    def seek(self, cookie: int):
        self.file.seek(cookie)
        self.tmp.seek(cookie)
        self.tmp.truncate()

    def readline(self) -> str:
        self.line = self.file.readline().strip()
        return self.line

    def write(self, payload: str) -> int:
        return self.tmp.write(payload)

    def close(self):
        self.readline()
        while len(self.line) != 0:
            self.write(self.line + '\n')
            self.readline()
        self.file.close()
        self.tmp.close()

        self.tmp_path.rename(self.path.name)
