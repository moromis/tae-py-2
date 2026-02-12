from player.history import History

NOTHING_TO_UNDO = "You have to actually enter a command first."


def undo(**kwargs):
    """Undo the last user command"""
    if len(History.get_history()) == 0:
        return NOTHING_TO_UNDO
    cmd = History.undo_latest_command()
    return f'Reverted "{cmd}"'
