from editor.editor import main_loop as main_editor_loop
from shared import cls, prompt
from strings import STARTUP, SELECT_EDITOR_OR_PLAYER


def main():
    cls()
    print(STARTUP)
    print(SELECT_EDITOR_OR_PLAYER)
    selection = prompt()
    if selection == "1":
        cls()
        main_editor_loop()
    else:
        cls()
        main()


if __name__ == "__main__":
    main()