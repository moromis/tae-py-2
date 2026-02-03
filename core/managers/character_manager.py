from core import Writeable, Character


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


def set_characters_json(new_characters: dict[str, Character | dict]) -> None:
    global characters
    sanitized_characters = {}
    for n, o in new_characters.items():
        if not isinstance(o, Character):
            obj = Character(n)
            obj.from_dict(o)
            sanitized_characters[n] = obj
    characters = sanitized_characters


def get_character_by_name(name: str) -> Character | None:
    global characters
    name = name.lower()
    for char_key, char in characters.items():
        if char_key == name:
            return char
