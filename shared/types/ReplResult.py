from strings import BASE_PATH


class ReplResult:
    def __init__(
        self, path: str = BASE_PATH, clear: bool = False, replace: bool = False
    ):
        self.path = path
        self.clear = clear
        self.replace = replace
