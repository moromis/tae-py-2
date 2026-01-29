from shared import Writeable, Character


characters: dict[str, Character] = {}


def get_characters():
    global characters
    return characters


def get_characters_json():
    global characters
    return {
        n: c.to_dict() if isinstance(c, Writeable) else c for n, c in characters.items()
    }


def add_character(character: Character):
    global characters
    characters[character.name] = character


def set_characters(new_characters: dict[str, Character]) -> None:
    global characters
    characters = new_characters
