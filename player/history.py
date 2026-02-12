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

    @classmethod
    def get_pretty_last_ten(cls):
        ret = ""
        if len(cls.history) > 0:
            ret += f"- {cls.history[0]}"
        if len(cls.history) > 1:
            ret += "\n- ".join(cls.history[1:10])
