class History:
    def __init__(self) -> None:
        self.history: list[str] = []

    def push_history(self, command: str):
        self.history.append(command)

    def get_latest_command(self):
        return self.history[-1]

    def undo_latest_command(self):
        return self.history.pop()

    def get_history(self) -> list[str]:
        return self.history
