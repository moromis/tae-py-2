class History:

    history: list[str] = []

    @classmethod
    def push_history(cls, command: str):
        cls.history.append(command)

    @classmethod
    def get_latest_command(cls):
        return cls.history[-1]

    @classmethod
    def undo_latest_command(cls):
        return cls.history.pop()

    @classmethod
    def get_history(cls) -> list[str]:
        return cls.history

    @classmethod
    def reset(cls):
        cls.history = []
