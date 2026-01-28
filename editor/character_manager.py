from shared.types.Character import Character


characters = {}


def get_characters():
    return characters


def add_character(character: Character):
    characters[character.name] = character
